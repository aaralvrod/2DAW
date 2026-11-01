const prompt = require("prompt-sync")();
const numeroSecreto = Math.floor(Math.random() * 50) + 1;
let intentos = 5;
function jugar() {
    const respuesta = parseInt(prompt("Adivina el número entre 1 y 50:"));

if (respuesta === numeroSecreto) {
    console.log("¡Felicidades! Has adivinado el número.");
    return; // Finaliza el juego
} else if (respuesta > numeroSecreto) {
    console.log("El número secreto es menor.");
} else {
    console.log("El número secreto es mayor.");
}

intentos--;

if (intentos === 0) {
    console.log("Se te han acabado los intentos. El número era " + numeroSecreto);
} else {
    jugar(); // Llamamos de nuevo a la función si quedan intentos
}
}

jugar();