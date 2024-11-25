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
    "zh-CN": {
        correct: "回答正确！",
        incorrect: "回答错误！",
        next_question: "下一题",
        prev_question: "上一题",
        explanation: "点击查看答案解析",
    },
};

// Detect the current language
// Detect the current language from the URL
const urlPath = window.location.pathname; // Get the URL path
let currentLanguage = urlPath.includes('/zh-cn/') ? "zh-cn" : "en"; // Default to "en"

// Update the <html> lang attribute dynamically
document.documentElement.lang = currentLanguage;
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



document.addEventListener("DOMContentLoaded", function () {
    // Extract the total number of questions from the page-indicator span
    const pageIndicator = document.querySelector(".page-indicator");
    if (!pageIndicator) return; // Exit if the page-indicator is not found

    const totalQuestionsMatch = pageIndicator.textContent.match(/\/\s*(\d+)/); // Match "1 / 200"
    const totalQuestions = totalQuestionsMatch ? parseInt(totalQuestionsMatch[1], 10) : 0;

    if (totalQuestions > 0) {
        document.addEventListener("keydown", function (event) {
            // Extract the current question number from the page-indicator
            const currentQuestionMatch = pageIndicator.textContent.match(/(\d+)\s*\/\s*\d+/); // Match "1 / 200"
            const currentQuestion = currentQuestionMatch ? parseInt(currentQuestionMatch[1], 10) : 0;

            if (event.key === "ArrowRight" && currentQuestion < totalQuestions) {
                // Navigate to the next question
                const nextQuestion = currentQuestion + 1;
                window.location.href = `q${nextQuestion}.html`;
            } else if (event.key === "ArrowLeft" && currentQuestion > 1) {
                // Navigate to the previous question
                const prevQuestion = currentQuestion - 1;
                window.location.href = `q${prevQuestion}.html`;
            }
        });
    }
});