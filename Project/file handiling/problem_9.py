# A program to save dictionary as JSON FILE

import json


student = {
    "name": "Kishan",
    "age": 16,
    "grade": "10",
    "marks": {
        "math": 85,
        "science": 90
    }
}

# Save the dictionary to a JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)  # indent=4 makes it pretty

print("Dictionary saved to student.json")

# Read the dictionary back from the JSON file
with open("student.json", "r") as file:
    loaded_student = json.load(file)

print("\nLoaded Dictionary from JSON:")
print(loaded_student)

