let resultado;
const num1 = parseInt(process.argv[3])
const num2 = parseInt(process.argv[4])
let historial = []
let fecha = Date().toString()
switch(process.argv[2]) {
    case "+":
        resultado = num1 + num2;
        console.log(`${num1} + ${num2} = ${resultado}`);
        historial.push(`${num1} + ${num2}, resultado = ${resultado} | ${fecha}`)
            console.log("Historial -> " + historial)
        break;
    case "-":
        resultado = num1 - num2;
        console.log(`${num1} - ${num2} = ${resultado}`);
        historial.push(`${num1} - ${num2}, resultado = ${resultado} | ${fecha}`)
            console.log("Historial -> " + historial)
        break;
    case "*":
        resultado = num1 * num2;
        console.log(`${num1} * ${num2} = ${resultado}`);
        historial.push(`${num1} * ${num2}, resultado = ${resultado} | ${fecha}`)
            console.log("Historial -> " + historial)
        break;
    case "/":
        resultado = num1 / num2;
        console.log(`${num1} / ${num2} = ${resultado}`);
        historial.push(`${num1} / ${num2}, resultado = ${resultado} | ${fecha}`)
            console.log("Historial -> " + historial)
        break;
    case "%":
        resultado = num1 % num2;
        console.log(`${num1} % ${num2} = ${resultado}`);
        historial.push(`${num1} % ${num2}, resultado = ${resultado} | ${fecha}`)
            console.log("Historial -> " + historial)
        break;
    case "^":
        resultado = Math.pow(num1, num2);
        console.log(`${num1} ^ ${num2} = ${resultado}`);
        historial.push(`${num1} ^ ${num2}, resultado = ${resultado} | ${fecha}`)
            console.log("Historial -> " + historial)
        break;
    case "raiz":
        if (num1 < 0) {
            console.log("No se permiten numeros negativos")
            break;
        }
        else if(num2 < 0) {
            console.log("No se permiten numeros negativos")
            break;
        }
        else {
        resultado = Math.pow(num1, 1/num2);
        console.log(`${num1} ^ 1/${num2} = ${resultado}`);
        historial.push(`${num1} ^ 1/${num2}, resultado = ${resultado} | ${fecha}`)
            console.log("Historial -> " + historial)
        break;
        }

    default:
        resultado = "Operacion no valida"
}
