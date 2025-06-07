function correctUserPassword() {
  const correctPassword = "1234";
  let attempts = 0;
  let input;

  do {
    input = prompt("შეიყვანეთ პაროლი:");
    attempts++;
  } while (input !== correctPassword);

  alert("correct guess. ცდების რაოდენობა: " + attempts);
}

correctUserPassword();
