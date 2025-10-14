let myObj = {
    name: "David",
    surname: "Tezelashvili",
    academy: "GOA",
    isMentor: true,
    num: 100,
    hobbies: ["programming", "bike", "basketball"],
    favColor: "Blue"
}

let list = document.getElementById("myList");

for (let key in myObj) {
    let liKey = document.createElement("li");
    liKey.textContent = key;

    let liValue = document.createElement("li");
    liValue.textContent = Array.isArray(myObj[key]) ? myObj[key].join(", ") : myObj[key];

    list.appendChild(liKey);
    list.appendChild(liValue);
}
