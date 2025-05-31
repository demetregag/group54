const person = {
name: "deme",
surname: "gagnidze",
academy: "Web Academy",
role: "Student",
city: "Tbilisi",
favColor: "Blue",
favLanguage: "JavaScript",
sayHello: function() {
console.log("Hello")
},
showProperty: function() {
console.log(this.favLanguage)
}
}
console.log(person)
console.log(person.city)
person.favColor = "Green"
console.log(person.favColor)
person.sayHello()
