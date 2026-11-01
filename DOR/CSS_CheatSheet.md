# 🎨 CSS Cheat Sheet

Una guía rápida y explicada con lo esencial de **CSS**, incluyendo: selectores, modelo de cajas, posicionamiento, flexbox, grid, animaciones y responsive design.

---

## 📌 1. Selectores Básicos
Permiten aplicar estilos a diferentes elementos en HTML.

```css
/* Elemento */
p { color: red; }

/* Clase (.) */
.texto { font-size: 18px; }

/* ID (#) */
#principal { background: lightblue; }

/* Descendiente */
div p { color: green; }

/* Hijo directo */
div > p { font-weight: bold; }

/* Hermano adyacente */
h1 + p { color: gray; }

/* Hermano general */
h1 ~ p { font-style: italic; }

/* Pseudo-clases */
a:hover { color: orange; }        /* al pasar el ratón */
input:focus { border: 2px solid blue; } /* al enfocar input */
li:first-child { color: red; }    /* primer hijo */
li:last-child { color: blue; }    /* último hijo */
```

---

## 📌 2. Modelo de Caja (Box Model)

En CSS **todo es una caja**. Cada elemento tiene:

```
+-------------------------+
|       margin            |   ← Espacio externo
+-------------------------+
|       border            |   ← Borde
+-------------------------+
|       padding           |   ← Espacio interno
+-------------------------+
|       content           |   ← Contenido (texto, imagen...)
+-------------------------+
```

Ejemplo en CSS:

```css
.caja {
  width: 200px;              /* ancho del contenido */
  height: 100px;             /* alto del contenido */
  padding: 20px;             /* espacio interno */
  border: 5px solid black;   /* borde */
  margin: 10px;              /* espacio externo */
  box-sizing: border-box;    /* incluye padding y border en width/height */
}
```

👉 Usar `box-sizing: border-box;` es lo más recomendado.

---

## 📌 3. Posicionamiento de Cajas

Define cómo se colocan los elementos en la página:

- **static** → por defecto, sigue el flujo normal.
- **relative** → relativo a su posición original.
- **absolute** → relativo al contenedor más cercano con `position: relative`.
- **fixed** → fijo en la ventana (aunque hagas scroll).
- **sticky** → mezcla entre relative y fixed (se queda pegado al llegar a un punto).

Ejemplo:

```css
.padre {
  position: relative;
}

.hijo {
  position: absolute;
  top: 0;
  right: 0;
}
```

---

## 📌 4. Posicionar el Contenido dentro de una Caja

### 🔹 Alineación de texto
```css
.caja {
  text-align: center;   /* center | left | right | justify */
  vertical-align: middle; /* para inline o tablas */
}
```

### 🔹 Con Flexbox
```css
.caja {
  display: flex;
  justify-content: center; /* eje horizontal */
  align-items: center;     /* eje vertical */
}
```

### 🔹 Con Grid
```css
.caja {
  display: grid;
  place-items: center; /* centra en ambos ejes */
}
```

---

## 📌 5. Tipografía y Texto

```css
font-family: Arial, sans-serif;
font-size: 16px;
font-weight: bold;        /* normal, bold, 100–900 */
font-style: italic;       /* cursiva */
text-align: center;       /* left, right, center, justify */
text-decoration: underline;
line-height: 1.5;         /* interlineado */
letter-spacing: 2px;      /* espacio entre letras */
```

---

## 📌 6. Colores y Fondos

```css
color: #333; /* color de texto */
background-color: lightyellow;
background-image: url('imagen.jpg');
background-size: cover;   /* ocupa todo el contenedor */
background-position: center;
background-repeat: no-repeat;
```

---

## 📌 7. Layout (Display & Position)

```css
/* Display */
display: block;        /* ocupa toda la línea */
display: inline;       /* en línea */
display: inline-block; /* en línea con tamaño */
display: flex;         /* sistema flexible */
display: grid;         /* sistema de cuadrícula */
display: none;         /* no se muestra */

/* Posicionamiento adicional */
top: 0;
left: 0;
z-index: 10;           /* orden de apilado */
```

---

## 📌 8. Flexbox

```css
.container {
  display: flex;
  flex-direction: row;     /* row | column */
  justify-content: center; /* flex-start, space-between */
  align-items: center;     /* stretch, flex-start, center */
  gap: 10px;
}

.item {
  flex: 1; /* ocupa espacio proporcional */
}
```

---

## 📌 9. Grid

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 columnas iguales */
  grid-template-rows: auto;
  gap: 10px;
}

.item {
  grid-column: span 2; /* ocupa 2 columnas */
  grid-row: span 1;
}
```

---

## 📌 10. Transiciones y Animaciones

```css
/* Transiciones */
button {
  transition: all 0.3s ease-in-out; /* suaviza cambios */
}
button:hover {
  transform: scale(1.1);
  background: lightblue;
}

/* Animaciones */
@keyframes mover {
  0% { transform: translateX(0); }
  100% { transform: translateX(100px); }
}
.caja {
  animation: mover 2s infinite alternate;
}
```

---

## 📌 11. Responsive Design

Permite adaptar el diseño a pantallas pequeñas.

```css
@media (max-width: 768px) {
  body {
    font-size: 14px;
  }
}
```

---

## 📌 12. Unidades de Tamaño

### 🔹 Absolutas
- `px` → píxeles fijos.

### 🔹 Relativas al contenedor
- `%` → relativo al tamaño del padre.

### 🔹 Relativas al texto
- `em` → relativo al tamaño de la fuente del **elemento actual**.
- `rem` → relativo al tamaño de fuente de `html`.

### 🔹 Relativas a la ventana (viewport)
- `vw` → ancho de la ventana (`100vw` = todo el ancho).
- `vh` → alto de la ventana (`100vh` = toda la altura).
- `vmin`, `vmax` → relativo al lado más pequeño o más grande.

Ejemplo pantalla completa:

```css
.fullscreen {
  width: 100vw;
  height: 100vh;
}
```

---

## ✅ Conclusión

Esta cheat sheet contiene lo esencial de CSS:  
- **Selectores**  
- **Modelo de cajas**  
- **Posicionamiento de cajas y contenido**  
- **Tipografía, colores y fondos**  
- **Layouts con display, flexbox y grid**  
- **Transiciones y animaciones**  
- **Responsive design y unidades de tamaño**  

Es una referencia rápida y práctica para proyectos en CSS.
