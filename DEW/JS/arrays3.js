let peliculas = []
let seleccionada = null

function agregarPelicula(nombre){
    if((typeof nombre !== 'string') || (nombre.trim() == "") || nombre == null || nombre == undefined){
        return;
    }
    peliculas.push(nombre);
}

function borrarPelicula(nombre){
    const indx = peliculas.indexOf(nombre);
    if(indx !== -1) peliculas.splice(indx,1);
}

function mostrarPeliculas(){
    peliculas.forEach(p =>(
        console.log(p);
    ));
}


agregarPelicula("007", "Alien");
console.log(peliculas);
borrarPelicula("007");
console.log(peliculas);