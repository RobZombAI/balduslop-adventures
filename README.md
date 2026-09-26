# Claybound (Clone Completo)

Clon completo y autónomo del juego web de plataformas en 3D **Claybound** ([https://claybound-56949.web.app/](https://claybound-56949.web.app/)).

## 🎮 Acerca del juego
Claybound es un juego de plataformas 3D realizado en Three.js con estética de plastilina / modelado en arcilla, que permite moldear rampas, puentes y explorar cañones, bosques, cavernas y reinos de ensueño.

## 📁 Estructura del proyecto
- [index.html](file:///Users/robzomb/Documents/antigravity/elegant-lovelace/index.html): Documento HTML principal y contenedor del canvas WebGL.
- [manifest.webmanifest](file:///Users/robzomb/Documents/antigravity/elegant-lovelace/manifest.webmanifest): Manifiesto PWA para instalación web móvil y de escritorio.
- `bundle/`:
  - `index-B9TPSTBI.js`: Lógica principal del motor, física, niveles y renderizado Three.js.
  - `index-DjewJEKc.css`: Estilos, animaciones e interfaz de usuario.
  - Fuentes tipográficas (`.woff`): Clay Display, Clay Sans, Hand.
  - Efectos de sonido (`.wav`): Pasos, saltos, impactos, mecanismos, cascadas, criaturas.
  - Música ambiental (`.mp3`): Bandas sonoras de los biomas.
  - Módulos analíticos opcionales (`posthog-*.js`, `ga4-*.js`).
- `assets/`:
  - Modelos 3D (`.glb`): Personajes, escenarios (cañón, bosque, caverna, sueño, mármol), enemigos y jefe *Mother Puff*.
  - Texturas e imágenes (`.webp`, `.jpg`, `.png`): Mapas de resplandor (glow), acabados y tarjetas de capítulos.
  - Configuraciones y animaciones (`.json`): Animaciones de esqueletos de personajes, enemigos y datos de tarjetas.
  - `third-party-licenses.txt`: Licencias de librerías de código abierto utilizadas (Three.js, Lucide, etc.).

## 🚀 Cómo ejecutar localmente

Al tratarse de una aplicación cliente estática con WebGL y Web Workers, se debe servir mediante un servidor HTTP local para evitar restricciones CORS en navegadores:

### Opción 1: Python
```bash
python3 -m http.server 8080
```
Luego abre tu navegador en: [http://localhost:8080](http://localhost:8080)

### Opción 2: Node.js (npx serve)
```bash
npx serve .
```

### Opción 3: VS Code / Live Server
Abre la carpeta en VS Code y haz clic en "Go Live" o utiliza la extensión Live Server.
