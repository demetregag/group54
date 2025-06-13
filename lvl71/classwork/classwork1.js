function generateParagraph() {
    const div = document.getElementById('myDiv');
    const paragraph = document.createElement('p');
    paragraph.textContent = 'ეს არის ახალი პარაგრაფი.';
    div.appendChild(paragraph);
}
generateParagraph();