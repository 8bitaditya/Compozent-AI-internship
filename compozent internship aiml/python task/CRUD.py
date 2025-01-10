# Dictionary to store student data
students = {
    '101': {'name': 'Alice', 'age': 20, 'grades': ['A', 'B', 'A']},
    '102': {'name': 'Bob', 'age': 22, 'grades': ['B', 'B', 'C']},
    '103': {'name': 'Charlie', 'age': 21, 'grades': ['A', 'A', 'A']}
}

# Function to create or add a new student
def create_student():
    student_id = input("Enter student ID: ")
    
    if student_id in students:
        print(f"Student with ID {student_id} already exists.")
    else:
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        grades = input("Enter student's grades (comma-separated): ").split(',')
        
        # Store student data in the dictionary
        students[student_id] = {'name': name, 'age': age, 'grades': grades}
        print(f"Student {name} has been added.")

# Function to read/view a student's details
def read_student():
    student_id = input("Enter student ID to view details: ")
    
    if student_id in students:
        student = students[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grades: {', '.join(student['grades'])}")
    else:
        print(f"No student found with ID {student_id}")

# Function to update an existing student's details
def update_student():
    student_id = input("Enter student ID to update details: ")
    
    if student_id in students:
        print("Update student's details:")
        name = input(f"Enter new name (current: {students[student_id]['name']}): ")
        age = int(input(f"Enter new age (current: {students[student_id]['age']}): "))
        grades = input(f"Enter new grades (current: {', '.join(students[student_id]['grades'])}): ").split(',')
        
        # Update the dictionary with new values
        students[student_id] = {'name': name, 'age': age, 'grades': grades}
        print(f"Student {student_id}'s details have been updated.")
    else:
        print(f"No student found with ID {student_id}")

# Function to delete a student's record
def delete_student():
    student_id = input("Enter student ID to delete: ")
    
    if student_id in students:
        del students[student_id]
        print(f"Student with ID {student_id} has been deleted.")
    else:
        print(f"No student found with ID {student_id}")

# Function to display all student data
def display_all_students():
    if not students:
        print("No students available.")
    else:
        for student_id, student in students.items():
            print(f"\nStudent ID: {student_id}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grades: {', '.join(student['grades'])}")

# Menu for CRUD operations
def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Student Details")
        print("3. Update Student Details")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            create_student()
        elif choice == '2':
            read_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_all_students()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

# Run the program
menu()

