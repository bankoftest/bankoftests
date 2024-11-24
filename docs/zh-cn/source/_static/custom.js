// Messages and Translations
const translations = {
    "en": {
        correct: "Correct!",
        incorrect: "Incorrect!",
        next_question: "Next Question",
        prev_question: "Previous Question",
        explanation: "Click to view explanation",
    },
    "zh-cn": {
        correct: "回答正确！",
        incorrect: "回答错误！",
        next_question: "下一题",
        prev_question: "上一题",
        explanation: "点击查看答案解析",
    },
};

// Detect the current language
const currentLanguage = document.documentElement.lang || "en";

// Replace placeholders dynamically in the DOM
document.addEventListener("DOMContentLoaded", () => {
    // Replace placeholders for explanation and navigation buttons
    document.body.innerHTML = document.body.innerHTML.replace(/\|next_question\|/g, translations[currentLanguage]?.next_question || "Next Question");
    document.body.innerHTML = document.body.innerHTML.replace(/\|prev_question\|/g, translations[currentLanguage]?.prev_question || "Previous Question");
    document.body.innerHTML = document.body.innerHTML.replace(/\|explanation\|/g, translations[currentLanguage]?.explanation || "Explanation");

    // Add a class to the body if on a question page
    if (document.querySelector('.question-page')) {
        document.body.classList.add('is-question-page');
    }
});

// Handle question interactions
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

    // Display a result message in the correct language
    const resultElement = document.getElementById(`${questionId}-result`);
    resultElement.innerText = isCorrect
        ? translations[currentLanguage]?.correct || "Correct!"
        : translations[currentLanguage]?.incorrect || "Incorrect.";

    // Style the result message
    resultElement.classList.add("result-message");
}