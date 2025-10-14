function bow() {
  let bi = prompt("შეიყვანეთ ტექსტი:");
  let bo = prompt("lower თუ upper:");

  if (bi === "lower") {
    console.log(bi.toLowerCase());
  } else if (bo === "upper" ) {
    console.log(bi.toUpperCase());
  }
}

console.log(bow)
