const btn = document.getElementById("btn");
let left = 0;

btn.addEventListener("click", function () {
  mysetInterval=setInterval(function () {
    left -= 50;
    btn.style.left = left + "px";
  }, 1000);
});
