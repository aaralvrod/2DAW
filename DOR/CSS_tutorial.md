# 📘 CSS Cheat Sheet

Una guía rápida con lo esencial de **CSS**, explicada brevemente y con ejemplos prácticos.  

---

## 🎨 Selectores Básicos
Permiten aplicar estilos a diferentes elementos en HTML.

```css
/* Selecciona todos los párrafos */
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
a:hover { color: orange; }      /* al pasar el ratón */
input:focus { border: 2px solid blue; } /* al enfocar input */
li:first-child { color: red; }  /* primer hijo */
li:last-child { color: blue; }  /* último hijo */

width: 200px;      /* ancho */
height: 100px;     /* alto */
margin: 10px;      /* espacio externo */
padding: 15px;     /* espacio interno */
border: 2px solid black; /* borde */
border-radius: 10px;     /* esquinas redondeadas */
box-sizing: border-box;  /* incluye padding y border en width/height */

color: #333; /* color de texto */
background-color: lightyellow;
background-image: url('imagen.jpg');
background-size: cover;   /* ocupa todo el contenedor */
background-position: center;
background-repeat: no-repeat;

font-family: Arial, sans-serif; /* tipografía */
font-size: 16px;                /* tamaño */
font-weight: bold;              /* grosor: normal, bold, 100–900 */
font-style: italic;             /* cursiva */
text-align: center;             /* alineación: left, right, justify */
text-decoration: underline;     /* subrayado */
line-height: 1.5;               /* interlineado */
letter-spacing: 2px;            /* espacio entre letras */


/* Display */
display: block;        /* ocupa toda la línea */
display: inline;       /* en línea */
display: inline-block; /* en línea con tamaño */
display: flex;         /* sistema flexible */
display: grid;         /* sistema de cuadrícula */
display: none;         /* no se muestra */

/* Posicionamiento */
position: static;   /* por defecto */
position: relative; /* relativo a sí mismo */
position: absolute; /* relativo al contenedor */
position: fixed;    /* fijo en la ventana */
position: sticky;   /* se queda pegado */
top: 0; left: 0;
z-index: 10;        /* orden de apilado */

.container {
  display: flex;
  flex-direction: row;     /* row | column */
  justify-content: center; /* eje principal: flex-start, space-between */
  align-items: center;     /* eje secundario: stretch, center */
  gap: 10px;               /* espacio entre hijos */
}

.item {
  flex: 1; /* ocupa espacio proporcional */
}


.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 columnas iguales */
  grid-template-rows: auto;
  gap: 10px;
}

.item {
  grid-column: span 2; /* ocupa 2 columnas */
  grid-row: span 1;    /* ocupa 1 fila */
}


/* Transiciones */
button {
  transition: all 0.3s ease-in-out; /* suaviza cambios */
}
button:hover {
  transform: scale(1.1);  /* agranda */
  background: lightblue;
}

/* Animaciones */
@keyframes mover {
  0% { transform: translateX(0); }
  100% { transform: translateX(100px); }
}
.caja {
  animation: mover 2s infinite alternate; /* rebote infinito */
}


@media (max-width: 768px) {
  body {
    font-size: 14px; /* texto más pequeño en móviles */
  }
}


