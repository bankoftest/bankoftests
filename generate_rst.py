import json
import os

# Define a dictionary to manage multiple datasets
paths_dataset = {
    "math_test_elementary_school_grade_one_zh": {
        "testbank_file": "testbanks/math_test_elementary_school_grade_one_zh.json",
        "rst_dir": "docs/zh-cn/source/math_test/elementary_school/grade_one",
        "image_dir": "../../../images/math_test/elementary_school/grade_one"
    },
    "math_test_elementary_school_grade_one_en": {
        "testbank_file": "testbanks/math_test_elementary_school_grade_one_en.json",
        "rst_dir": "docs/en/source/math_test/elementary_school/grade_one",
        "image_dir": "../../../images/math_test/elementary_school/grade_one"
    },
    "driver_test_ca_bc_zh": {
        "testbank_file": "testbanks/driver_test_ca_bc_zh.json",
        "rst_dir": "docs/zh-cn/source/driver_test/ca/bc",
        "image_dir": "../../../images/driver_test/ca/bc"
    },
    "driver_test_ca_bc_en": {
        "testbank_file": "testbanks/driver_test_ca_bc_en.json",
        "rst_dir": "docs/en/source/driver_test/ca/bc",
        "image_dir": "../../../images/driver_test/ca/bc"
    },
}


def write_question_rst(question, rst_dir, total_questions, title, image_dir):
    question_id = f"q{question['id']}"  # Unique ID for the question
    filename = f"{question_id}.rst"
    filepath = os.path.join(rst_dir, filename)

    # Determine the previous and next question IDs
    prev_question = f"q{question['id'] - 1}" if question['id'] > 1 else None
    next_question = f"q{question['id'] + 1}" if question['id'] < total_questions else None

    # Write question content
    with open(filepath, "w", encoding="utf-8") as f:
        # Add the test title as a heading
        f.write(".. raw:: html\n\n")
        f.write("   <div class=\"question-page\">\n")  # Open a unique div for the page

        # Add the test name
        f.write(f"   <div class=\"test-name\">{title}</div>\n\n")

        # Write meta information for SEO
        write_meta(f, question['question'], question.get("meta_keywords", ""))  # Use question for description

        # Add the question-card wrapper
        f.write(".. raw:: html\n\n")
        f.write("   <div class=\"question-card\">\n\n\n")  # Open the question-card div

        # Write question title
        question_title = f"{question['question']}"
        write_title(f, question_title)

        # Add a horizontal line (hr) below the title
        f.write(".. raw:: html\n\n")
        f.write("   <hr>\n\n")

        # Add image if available
        if "image" in question:
            image_path = os.path.join(image_dir, question['image'])
            f.write(f".. image:: /{image_path}\n")
            f.write("   :width: 70%\n")
            f.write("   :alt: Image for the question\n")
            f.write("   :class: question-image\n")  # Apply the custom CSS class
            f.write("   :align: center\n")  # Aligns the image in the center
            f.write("\n\n\n")  # Adds a blank line after the image block

        # Write options with interactive buttons
        write_interactive_html(f, question_id, question['options'], question['answer'])

        f.write("   <hr>\n") 
        # Write explanation (hidden by default)
        f.write("\n.. dropdown:: ►|explanation|\n\n")
        f.write(f"   {question['explanation']}\n")

        # Add navigation buttons
        f.write("\n.. raw:: html\n\n")
        if prev_question is None and next_question:  # Only "Next Question" exists
            f.write("   <div class=\"nav-buttons single-next\">\n")
        else:
            f.write("   <div class=\"nav-buttons\">\n")

        if prev_question:
            # Insert placeholder for "Previous Question"
            f.write(f"       <a href=\"{prev_question}.html\" class=\"button\">|prev_question|</a>\n")

        # Add the page indicator
        f.write(f"       <span class=\"page-indicator\">{question['id']} / {total_questions}</span>\n")

        if next_question:
            # Insert placeholder for "Next Question"
            f.write(f"       <a href=\"{next_question}.html\" class=\"button\">|next_question|</a>\n")

        f.write("   </div>\n")  # Close nav-buttons

        # Close the question-card div
        f.write("   </div>\n\n")

        # Close the question-page div
        f.write("   </div>\n")


# Function to write meta information for SEO
def write_meta(file, description, keywords):
    file.write(".. meta::\n")
    file.write(f"   :description: {description}\n")
    file.write(f"   :keywords: {keywords}\n\n")


# Function to write the title with underline
def write_title(file, title):
    file.write(f"{title}\n")
    file.write("=" * (len(title) * 2) + "\n\n")


# Function to write interactive HTML content
# Function to write interactive HTML content
def write_interactive_html(file, question_id, options, correct_answer):
    file.write(".. raw:: html\n\n")
    file.write(f"   <div id=\"{question_id}\" class=\"quiz\">\n")
    
    # Iterate over options dictionary (letter keys and option text values)
    for letter, option_text in options.items():
        is_correct = "true" if letter == correct_answer else "false"

        # HTML for the interactive option
        file.write(f"       <div class=\"option\" id=\"{question_id}-{letter}\" onclick=\"selectOption('{question_id}', '{letter}', {is_correct})\">\n")
        file.write(f"           {letter}. {option_text}\n")  # Display letter and option text
        file.write("       </div>\n")
    
    file.write(f"       <p id=\"{question_id}-result\" class=\"result\"></p>\n")
    file.write("   </div>\n\n")


# Function to update the index.rst file with a toctree
def update_toctree(title, questions, rst_dir):
    index_path = os.path.join(rst_dir, "index.rst")
    with open(index_path, "w", encoding="utf-8") as index_file:
        # Write the title and its underline
        index_file.write(f"{title}\n")
        index_file.write("=" * (len(title) * 2) + "\n\n")

        # Write the toctree
        index_file.write(".. toctree::\n")
        index_file.write("   :maxdepth: 2\n\n")
        for question in questions:
            question_id = f"q{question['id']}"
            index_file.write(f"   {question_id}\n")


# Main script logic
def main(test_id):
    # Check if the test ID is valid
    if test_id is None:
        print("No test id input.")
        return

    if test_id not in paths_dataset:
        print(f"Test ID '{test_id}' not found in paths_dataset.")
        return

    # Load dataset parameters
    selected_test = paths_dataset[test_id]
    testbank_file = selected_test["testbank_file"]
    rst_dir = selected_test["rst_dir"]
    image_dir = selected_test["image_dir"]

    # Load questions from JSON
    with open(testbank_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Extract questions and title
    questions = data["questions"]
    title = data.get("title", "Questions")
    total_questions = len(questions)

    # Ensure output directory exists
    os.makedirs(rst_dir, exist_ok=True)

    # Generate `.rst` files for each question
    for question in questions:
        write_question_rst(question, rst_dir, total_questions, title, image_dir)

    # Update the toctree in the index.rst file with the title
    update_toctree(title, questions, rst_dir)


if __name__ == "__main__":
    #test_id = "driver_test_ca_bc_en"  
    #test_id = "driver_test_ca_bc_zh"
    test_id = None

    main(test_id)