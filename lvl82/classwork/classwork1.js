const num = function(num1) {
  for (let key in num1) {
    console.log(num1[key]);
  }
};

const person = {
  name: "deme",
  age: 11,
  city: "tbilysi"
};

num(person);
