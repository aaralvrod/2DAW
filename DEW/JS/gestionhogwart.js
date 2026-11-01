let estudiantes = []
let estudiante = new Object();
    estudiante.nombre = 'manolo';
    estudiante.casa = 'Hogwart'

function Estudiante(nombre, casa, edad) {
    this.nombre = nombre;
    this.casa = casa;
    this.edad = edad;

    this.presentarse = function () {
        console.log(`Hola, soy ${this.nombre}, tengo ${this.edad} años y pertenezco a la casa ${this.casa}.`);
    };
}