const result = ((arr) => {
  return arr.reduce((product, num) => product * num, 1);
})([2, 3, 4]);

console.log(result);
