function checkLogin() {
  let value = document.getElementById("loginInput").value;

  if (value === "true") {
    alert("logged in");
  } else {
    alert("try again");
  }
}