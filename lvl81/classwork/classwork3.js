function checkValues(a, b, c, d, e, f, g, h, i, j) {
  for (let item of arguments) {
    if (typeof item === "number") console.log(item);
    else console.log(1);
  }
}

checkValues(10, "hi", 20, "js", 30, "code", 40, "test", 50, "go");
