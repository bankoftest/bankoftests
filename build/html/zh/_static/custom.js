// Messages for results
const messages = {
    correct: "Correct!",
    incorrect: "Incorrect."
};

document.addEventListener("DOMContentLoaded", () => {
    // Check if .question-page exists in the document
    if (document.querySelector('.question-page')) {
        // Add a class to the body to indicate it's a question page
        document.body.classList.add('is-question-page');
    }
});

function selectOption(questionId, selectedLetter, isCorrect) {
    // Clear previous styles
    const options = document.querySelectorAll(`#${questionId} .option`);
    options.forEach(option => {
        option.classList.remove("correct", "incorrect"); // Reset styles
        option.innerHTML = option.innerHTML.replace("👍", "").replace("👎", ""); // Remove emojis
    });

    // Highlight the selected option
    const selectedOption = document.querySelector(`#${questionId}-${selectedLetter}`);
    if (isCorrect) {
        selectedOption.classList.add("correct");
        selectedOption.innerHTML += " 👍";
    } else {
        selectedOption.classList.add("incorrect");
        selectedOption.innerHTML += " 👎";
    }

    // Display a result message
    const resultElement = document.getElementById(`${questionId}-result`);
    resultElement.innerText = isCorrect ? messages.correct : messages.incorrect;

    // Style the result message
    resultElement.classList.add("result-message");
}