import json 

try:
    f = open('module-8/student.json')
    data = json.load(f)
    f.close()
except FileNotFoundError:
    print("Error! 'student.json' file not found!")
    exit()

def print_list(students):
    for student in students:
        print(f"{student['F_Name']} , {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

print("Original Student List")
print_list(data)

new_student = {
    "F_Name": "Adrian",
    "L_Name": "Marquez",
    "Student_ID": 123456,
    "Email": "admarquez@my365.bellevue.edu"
}

data.append(new_student)

print("\nUpdated Student List")
print_list(data)

# Not receiving a prompt to save the updated student list, so I created my own prompt.
# Entering yes will save the updated student list to 'student.json'.
save_changes = input("\nWould you like to save the updated student list to 'student.json'? (yes/no): ").strip().lower()

# Print the input for debugging purposes
print(f"User input after processing: '{save_changes}'")

if save_changes in ['yes', 'y']:
    # Save changes to the JSON file
    with open('student.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("\nThe jSON file has been updated.")
else: 
    print("\nThe file was not updated.")
