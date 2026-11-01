let resultado;
const num1 = parseInt(process.argv[3])
const num2 = parseInt(process.argv[4])
switch(process.argv[2]) {
    case "suma":
        resultado = num1 + num2;
        console.log(`${num1} + ${num2} = ${resultado}`);
        break;
    case "resta":
        resultado = num1 - num2;
        console.log(`${num1} - ${num2} = ${resultado}`);
        break;
    case "multiplicacion":
        resultado = num1 * num2;
        console.log(`${num1} * ${num2} = ${resultado}`);
        break;
    case "division":
        resultado = num1 / num2;
        console.log(`${num1} / ${num2} = ${resultado}`);
        break;
    default:
        resultado = "Operacion no valida"
}
