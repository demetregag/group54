const button = document.getElementById('myButton');
const div = document.getElementById('myDiv');
let clickCount = 0;
let colorTimeout;

button.addEventListener('click', () => {
clickCount++;
div.style.backgroundColor = 'red';
clearTimeout(colorTimeout);
colorTimeout = setTimeout(() => {
    div.style.backgroundColor = 'blue';
}, 10000);
div.style.left = (10 * clickCount) + 'px';
});