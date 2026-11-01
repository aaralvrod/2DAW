const readline = require("readline");
const param = process.argv;
let nombre;
let puntos;

// Ranking de cazadores
const cazadores = [
{ nombre: "Geralt", puntos: 95 },
{ nombre: "Lambert", puntos: 70 },
{ nombre: "Eskel", puntos: 80 },
{ nombre: "Vesemir", puntos: 85 },
{ nombre: "Ciri", puntos: 100 }
];

// Crear la interfaz de readline
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// funciones

function eliminarCazador(nombre) {
    cazadores.slice(nombre, 1);
}

function agregarCazador(nombre, puntos) {
    cazadores.push(nombre, puntos);
}

// Preguntar al usuario
rl.question("Ordenar por:\n1. Nombre\n2. Puntos\n3. Agregar Cazador\n4. Eliminar Cazador", (opcion) => {
    if (opcion === "1") {
        cazadores.sort((a, b) => a.nombre.localeCompare(b.nombre));
    } else if (opcion === "2") {
        cazadores.sort((a, b) => b.puntos - a.puntos);
    } else if (opcion === "3") {
        agregarCazador();
    } else if (opcion === "4") {
        eliminarCazador()
    } else {
        console.log("Opción no válida");
    }
    console.table(cazadores);
    rl.close(); // cerrar readline
});
