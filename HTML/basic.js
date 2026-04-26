// ARRAY
console.log("Sanya Khare \n TCA2357045");
let numbers = [10, 20, 30, 40, 50];
console.log("Using for loop:");
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

function findSum(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

let result = findSum(numbers);
console.log("Sum of array:", result);

console.log("Using while loop:");
let i = 0;
while (i < numbers.length) {
    console.log(numbers[i]);
    i++;
}