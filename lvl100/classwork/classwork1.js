const paragraph = document.getElementById('text');
const button = document.getElementById('colorBtn');

function chooseRandomColor(colors) {
  const idx = Math.floor(Math.random() * colors.length);
  return colors[idx];
}
const colorsArray = ['#e63946', '#2a9d8f', '#f4a261', '#457b9d', '#6a4c93'];

button.addEventListener('click', () => {
const color = chooseRandomColor(colorsArray);
paragraph.style.color = color;})
