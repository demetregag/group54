let count = 0;
const container = document.getElementById("name-container");

let intervalId = setInterval(() => {
    const p = document.createElement("p");
    p.textContent = "დემეტრე";
    container.appendChild(p);

    count++;
    if (count === 4) {
    clearInterval(intervalId);
    }
}, 5000);