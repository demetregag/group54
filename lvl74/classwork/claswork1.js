let colors = ["red", "blue", "green", "orange", "purple"];
let index = 0;

document.getElementById("colorBtn").onclick = function () {
  let button = this;
  let interval = setInterval(function () {
    button.style.backgroundColor = colors[index];
    index++;
    if (index === 5) {
      clearInterval(interval);
    }
  }, 2000);
}