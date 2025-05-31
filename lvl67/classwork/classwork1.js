document.getElementById('myForm').addEventListener('submit', function(event) {
event.preventDefault()
const form = document.getElementById('myForm')
const firstName = form.elements['firstName'].value
const email = form.elements['email'].value
const password = form.elements['password'].value
console.log(firstName)
console.log(email)
console.log(password)
})