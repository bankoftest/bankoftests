import json

# File path to the JSON file
json_file_path = "testbanks/driver_test_ca_bc_zh.json"

# Provided list of correct answers
correct_answers = """
C
D
A
C
B
C
B
A
B
A
B
D
C
D
C
A
D
D
A
C
B
A
B
D
D
B
D
D
C
D
D
C
A
C
A
B
A
B
B
A
A
C
A
B
A
C
A
A
D
A
B
C
C
A
D
A
C
C
C
C
C
D
D
C
B
C
C
B
A
D
C
C
A
B
A
A
D
B
D
D
D
C
A
D
D
D
B
A
A
C
A
A
C
C
A
B
C
D
A
B
C
A
C
A
D
B
D
C
B
D
A
B
A
D
A
B
A
C
D
A
A
A
B
B
A
B
D
D
B
B
B
A
C
D
C
B
A
B
B
C
A
A
A
D
C
A
B
B
B
B
D
B
D
C
B
D
B
C
B
B
B
B
C
B
B
D
B
B
B
C
A
D
C
C
C
B
B
C
A
C
C
A
B
C
C
A
B
B
A
B
A
B
B
C
B
B
D
C
C
A
""".strip().split("\n")

# Load the JSON data
with open(json_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract answers from the JSON
extracted_answers = [question['answer'] for question in data['questions']]

# Compare extracted answers with provided answers
if extracted_answers == correct_answers:
    print("All answers match!")
else:
    print("Some answers do not match.")
    # Find mismatches
    for i, (extracted, correct) in enumerate(zip(extracted_answers, correct_answers), start=1):
        if extracted != correct:
            print(f"Question {i}: Extracted answer = {extracted}, Correct answer = {correct}")