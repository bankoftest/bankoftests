import os
import json

def add_images_to_questions(json_file_path, images_path):
    """
    Add image filenames to questions in a JSON file if an image with a matching ID exists in the images folder.

    :param json_file_path: Path to the JSON file containing questions.
    :param images_path: Path to the folder containing images.
    """
    # Load the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Get a list of all images in the folder
    image_files = os.listdir(images_path)
    image_dict = {os.path.splitext(img)[0]: img for img in image_files}

    # Loop through the questions in the JSON and check for matching images
    for question in data.get("questions", []):
        question_id = str(question["id"])
        if question_id in image_dict:
            question["image"] = image_dict[question_id]

    # Save the updated JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f"Images added to questions in {json_file_path}")

if __name__ == "__main__":
    # Update these paths as needed
    json_file_path = "testbanks/driver_test_ca_bc_zh.json"
    images_path = "images/driver_test/ca/bc"

    add_images_to_questions(json_file_path, images_path)