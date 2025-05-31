function forConditions() {
let userNum = Number(prompt("Enter number:"));

if (userNum < 18) {
console.log("not adult");
} else if (userNum< 65) {
console.log("adult & not old");
} else if (userNum <= 113) {
console.log("retired");
} else {
console.log("lie");
}
}