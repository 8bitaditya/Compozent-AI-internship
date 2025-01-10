# Function to perform addition, subtraction, multiplication, and division
def perform_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2  
    return addition, subtraction, multiplication, division

# Taking input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Performing the operations
    addition, subtraction, multiplication, division = perform_operations(num1, num2)
    
    # Displaying the results
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")

except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

