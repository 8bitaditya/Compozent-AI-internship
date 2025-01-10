class Student:
    def __init__(self, name, age, grades):
        self.name = name          # Name of the student
        self.age = age            # Age of the student
        self.grades = grades      # List of grades

    def display_details(self):
        # Display the student's name, age, and grades
        print(f"\nStudent Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")

    def calculate_average(self):
        # Calculate the average of the grades
        if len(self.grades) == 0:
            return 0  # Prevent division by zero if no grades are available
        return sum(self.grades) / len(self.grades)


# Get user input for the student's details
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))

# Get grades as a space-separated string, then convert to a list of integers
grades_input = input("Enter student's grades (separate by space): ")
grades = list(map(int, grades_input.split()))

# Create the Student object
student = Student(name, age, grades)

# Display student details and calculate average grade
student.display_details()
average_grade = student.calculate_average()
print(f"Average Grade: {average_grade:.2f}")
