"""Generate a white, navy & gold contribution activity graph (last 31 days) as an animated SVG.

Usage: GITHUB_TOKEN=... python activity_graph.py <username> <output.svg>
"""
import json
import os
import sys
import urllib.request
from datetime import date

BG, NAVY, GOLD, TEXT, GRID = "#FFFFFF", "#1F2A44", "#C9A227", "#4A4A4A", "#ECEEF2"
DAYS = 31
W, H = 900, 320
LEFT, RIGHT, TOP, BOTTOM = 60, 30, 70, 50

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch_days(username, token):
    body = json.dumps({"query": QUERY, "variables": {"login": username}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as res:
        data = json.load(res)
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = [(d["date"], d["contributionCount"]) for w in weeks for d in w["contributionDays"]]
    return days[-DAYS:]


def render(days):
    counts = [c for _, c in days]
    top = max(max(counts), 4)
    plot_w, plot_h = W - LEFT - RIGHT, H - TOP - BOTTOM
    step = plot_w / (len(days) - 1)

    def x(i):
        return LEFT + i * step

    def y(v):
        return TOP + plot_h - v / top * plot_h

    points = [(x(i), y(c)) for i, c in enumerate(counts)]
    line = " ".join(f"{px:.1f},{py:.1f}" for px, py in points)
    area = f"{LEFT},{TOP + plot_h} {line} {x(len(days) - 1):.1f},{TOP + plot_h}"

    grid, labels = [], []
    for k in range(5):
        v = top * k / 4
        gy = y(v)
        grid.append(f'<line x1="{LEFT}" y1="{gy:.1f}" x2="{W - RIGHT}" y2="{gy:.1f}" stroke="{GRID}"/>')
        labels.append(f'<text class="axis" x="{LEFT - 12}" y="{gy + 4:.1f}" text-anchor="end">{round(v)}</text>')
    for i, (d, _) in enumerate(days):
        if i % 5 == 0 or i == len(days) - 1:
            day = date.fromisoformat(d)
            labels.append(f'<text class="axis" x="{x(i):.1f}" y="{H - BOTTOM + 22}" text-anchor="middle">{day:%b} {day.day}</text>')

    dots = "\n  ".join(
        f'<circle class="dot" cx="{px:.1f}" cy="{py:.1f}" r="4" style="animation-delay:{0.3 + i * 0.06:.2f}s"/>'
        for i, (px, py) in enumerate(points)
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Contribution activity, last {DAYS} days">
  <title>Contribution activity · last {DAYS} days</title>
  <style>
    .title {{ font: 700 20px "Segoe UI", Ubuntu, "Helvetica Neue", Arial, sans-serif; fill: {NAVY}; letter-spacing: 2px; }}
    .axis  {{ font: 400 11px "Segoe UI", Ubuntu, "Helvetica Neue", Arial, sans-serif; fill: {TEXT}; }}
    .line  {{ fill: none; stroke: {NAVY}; stroke-width: 3; stroke-linejoin: round;
              stroke-dasharray: 4000; stroke-dashoffset: 4000; animation: draw 2.4s ease-out .2s forwards; }}
    .area  {{ fill: url(#fade); opacity: 0; animation: show 1.2s ease-out 1.2s forwards; }}
    .dot   {{ fill: {GOLD}; stroke: {BG}; stroke-width: 2; opacity: 0; animation: show .4s ease-out forwards; }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes show {{ to {{ opacity: 1; }} }}
  </style>
  <defs>
    <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{GOLD}" stop-opacity=".35"/>
      <stop offset="100%" stop-color="{GOLD}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="{BG}" stroke="{GOLD}" stroke-width="1.5"/>
  <text class="title" x="{W / 2}" y="40" text-anchor="middle">CONTRIBUTION ACTIVITY · LAST {DAYS} DAYS</text>
  {"".join(grid)}
  {"".join(labels)}
  <polygon class="area" points="{area}"/>
  <polyline class="line" points="{line}"/>
  {dots}
</svg>
"""


if __name__ == "__main__":
    username, output = sys.argv[1], sys.argv[2]
    svg = render(fetch_days(username, os.environ["GITHUB_TOKEN"]))
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {output}")
