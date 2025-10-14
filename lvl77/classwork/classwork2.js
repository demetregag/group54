let boxes = document.querySelectorAll('.box');
boxes.forEach(box => {
    box.style.width = '60px';
    box.style.height = '60px';
    box.style.background = 'gray';
    box.style.borderRadius = '10px';
    box.style.margin = '10px';
    box.style.position = 'relative';
    box.style.left = '0px';
});
let x = 0;
function move() {
    x += 2;
    boxes.forEach(box => {
    box.style.left = x + 'px';
    });
    if (x < 300) requestAnimationFrame(move);
}
    move();