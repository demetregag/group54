let total = 0;

do {
  let input = prompt("Enter a number:");
  let number = Number(input);
  total += number;
} while (total <= 100);

alert("Total exceeded 100! Final total is: " + total);
