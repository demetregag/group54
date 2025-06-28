let b = document.getElementById('b');
let p = document.getElementById('id');

btn.addEventListener('click', function () {
    setInterval(function () {
      let size = parseInt(p.style.fontSize);
      p.style.fontSize = (size + 1) + 'px';
    }, 1000);
});