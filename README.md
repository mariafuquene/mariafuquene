<div align="center">

<img src="./assets/header.svg" alt="María Camila Fúquene Galvis — Frontend Developer" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=7F5AF0&center=true&vCenter=true&width=600&lines=%C2%A1Hola!+Soy+Mar%C3%ADa+Camila+%F0%9F%91%8B;Construyo+interfaces+con+HTML+y+CSS+%F0%9F%8E%A8;Doy+vida+a+la+web+con+JavaScript+%E2%9A%A1;Creo+componentes+reutilizables+con+React+%E2%9A%9B%EF%B8%8F" alt="Typing SVG"/>
</a>

<p>
  <img src="https://komarev.com/ghpvc/?username=mariafuquene&color=7f5af0&style=flat-square&label=Visitas" alt="Visitas al perfil"/>
  <a href="https://github.com/mariafuquene?tab=followers"><img src="https://img.shields.io/github/followers/mariafuquene?label=Seguidores&style=flat-square&color=e53170" alt="Seguidores"/></a>
</p>

</div>

---

## 👩‍💻 Sobre mí

```js
const maria = {
  nombre: "María Camila Fúquene Galvis",
  rol: "Frontend Developer",
  stack: ["HTML", "CSS", "JavaScript", "React"],
  aprendiendo: ["TypeScript", "Testing", "Accesibilidad web"],
  pasion: "Crear experiencias web bonitas, accesibles e interactivas",
  saludar() {
    return `¡Gracias por visitar mi perfil! 💜`;
  },
};
```

## 🛠️ Tecnologías

<div align="center">

<a href="https://developer.mozilla.org/es/docs/Web/HTML"><img src="https://skillicons.dev/icons?i=html" height="56" alt="HTML"/></a>&nbsp;
<a href="https://developer.mozilla.org/es/docs/Web/CSS"><img src="https://skillicons.dev/icons?i=css" height="56" alt="CSS"/></a>&nbsp;
<a href="https://developer.mozilla.org/es/docs/Web/JavaScript"><img src="https://skillicons.dev/icons?i=js" height="56" alt="JavaScript"/></a>&nbsp;
<a href="https://react.dev/"><img src="https://skillicons.dev/icons?i=react" height="56" alt="React"/></a>

<sub>Herramientas</sub><br/>
<img src="https://skillicons.dev/icons?i=git,github,vscode,vite,npm,figma&perline=6" alt="Herramientas"/>

</div>

## 🎯 ¿Qué sé hacer? <sub><sup>(haz clic en cada sección)</sup></sub>

<details>
<summary><b>🧱 HTML — estructura semántica y accesible</b></summary>
<br/>

- Etiquetas semánticas (`header`, `main`, `section`, `article`, `nav`, `footer`)
- Formularios con validación nativa
- Accesibilidad: atributos `aria-*`, `alt`, jerarquía de encabezados
- SEO básico con metaetiquetas

```html
<main>
  <section aria-labelledby="proyectos">
    <h2 id="proyectos">Mis proyectos</h2>
    <article class="card">
      <img src="proyecto.png" alt="Captura del proyecto" />
      <h3>Mi proyecto</h3>
    </article>
  </section>
</main>
```
</details>

<details>
<summary><b>🎨 CSS — diseño responsive y animaciones</b></summary>
<br/>

- Flexbox y CSS Grid
- Diseño responsive con *media queries* y unidades relativas
- Variables CSS, transiciones y `@keyframes`
- El banner animado de este perfil está hecho **solo con SVG + CSS** ([ver código](./assets/header.svg))

```css
:root { --primario: #7f5af0; }

.card {
  display: grid;
  gap: 1rem;
  border-radius: 1rem;
  transition: transform .3s ease, box-shadow .3s ease;
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 24px rgb(127 90 240 / .3);
}
```
</details>

<details>
<summary><b>⚡ JavaScript — lógica e interactividad</b></summary>
<br/>

- ES6+: *arrow functions*, desestructuración, *spread*, módulos
- Manipulación del DOM y eventos
- Asincronía con `Promise`, `async/await` y `fetch`
- Métodos de arreglos: `map`, `filter`, `reduce`

```js
const obtenerRepos = async (usuario) => {
  const res = await fetch(`https://api.github.com/users/${usuario}/repos`);
  const repos = await res.json();
  return repos
    .filter(({ fork }) => !fork)
    .map(({ name, stargazers_count }) => ({ name, estrellas: stargazers_count }));
};
```
</details>

<details>
<summary><b>⚛️ React — componentes y estado</b></summary>
<br/>

- Componentes funcionales y JSX
- Hooks: `useState`, `useEffect`, `useContext`, hooks personalizados
- Props, renderizado condicional y listas
- Proyectos con Vite

```jsx
import { useState } from "react";

export default function Saludo() {
  const [likes, setLikes] = useState(0);

  return (
    <button onClick={() => setLikes(likes + 1)}>
      💜 Me gusta este perfil: {likes}
    </button>
  );
}
```
</details>

## 📊 Estadísticas

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=mariafuquene&show_icons=true&theme=radical&hide_border=true&locale=es" alt="Estadísticas de GitHub"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=mariafuquene&layout=compact&theme=radical&hide_border=true&locale=es" alt="Lenguajes más usados"/>

<img src="https://streak-stats.demolab.com?user=mariafuquene&theme=radical&hide_border=true&locale=es" alt="Racha de contribuciones"/>

<img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=mariafuquene&theme=react-dark&hide_border=true&area=true" alt="Gráfico de actividad"/>

</div>

## 🐍 Mis contribuciones

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mariafuquene/mariafuquene/output/github-snake-dark.svg"/>
  <img src="https://raw.githubusercontent.com/mariafuquene/mariafuquene/output/github-snake.svg" alt="Serpiente comiendo mis contribuciones"/>
</picture>
</div>

## 🤝 Conectemos

<div align="center">

<a href="https://github.com/mariafuquene"><img src="https://img.shields.io/badge/GitHub-mariafuquene-181717?style=for-the-badge&logo=github" alt="GitHub"/></a>
<!-- Descomenta y completa con tu usuario de LinkedIn:
<a href="https://www.linkedin.com/in/TU-USUARIO/"><img src="https://img.shields.io/badge/LinkedIn-Conectemos-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn"/></a>
-->

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=110&section=footer" width="100%" alt=""/>

</div>
