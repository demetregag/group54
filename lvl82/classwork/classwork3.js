const reversed = (function(str) {
  return str.split('').reverse().join('');
})("hello");

console.log(reversed);
