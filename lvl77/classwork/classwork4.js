const div = document.createElement("div");
div.id = "myDiv";
div.style.backgroundColor = "lightblue";
div.style.width = "200px";
div.style.height = "200px";
div.style.marginBottom = "10px";
document.body.appendChild(div);

const button = document.createElement("button");
button.textContent = "დაწყება";
document.body.appendChild(button);

button.onclick = function() {
  div.style.backgroundColor = "tomato";
  let count = 1;
  let size = 200;
  const interval = setInterval(() => {
    const p = document.createElement("p");
    const text = document.createTextNode("p" + count);
    p.appendChild(text);
    document.body.appendChild(p);
    count++;
    size -= 20;
    if (size > 0) {
      div.style.width = size + "px";
      div.style.height = size + "px";
    } else {
      div.style.display = "none";
      clearInterval(interval);
    }
  }, 3000);
};