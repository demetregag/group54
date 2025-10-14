const array = ["deme", "school", 20, 5, true, false];

for (const item of array) {
  if (typeof item === "string") {
    console.log(item);
  } else if (typeof item === "number") {
    console.log(item + 10);
  } else if (typeof item === "boolean") {
    console.log(!item);
  }
}
