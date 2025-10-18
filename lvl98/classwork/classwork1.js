let numbers = [12, 75, 43, 21, 56, 8, 63, 19, 90, 27];

let greaterThan50 = numbers.find(num => num > 50);
console.log("First number greater than 50:", greaterThan50);

let divisibleBy7 = numbers.find(num => num % 7 === 0);
console.log("First number divisible by 7:", divisibleBy7);
