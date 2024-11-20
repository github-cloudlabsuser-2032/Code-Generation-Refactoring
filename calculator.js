// Define functions for each arithmetic operation
function add(x, y) {
    return x + y;
}

function subtract(x, y) {
    return x - y;
}

function multiply(x, y) {
    return x * y;
}

function divide(x, y) {
    if (y === 0) {
        return "Error! Division by zero.";
    }
    return x / y;
}

// Display the menu
function menu() {
    console.log("Select operation:");
    console.log("1. Add");
    console.log("2. Subtract");
    console.log("3. Multiply");
    console.log("4. Divide");
}

// Main program
while (true) {
    menu();
    const choice = prompt("Enter choice (1/2/3/4): ");

    if (['1', '2', '3', '4'].includes(choice)) {
        const num1 = parseFloat(prompt("Enter first number: "));