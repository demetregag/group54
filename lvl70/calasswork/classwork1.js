const button = document.getElementById('b');
function b() {
const userColor = prompt("შეიყვანე ფერი (მაგ: red, green, #00ff00):");
button.style.backgroundColor = userColor;
    }
button.addEventListener('click', b);