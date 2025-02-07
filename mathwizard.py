import math
import cmath
import os
import random
from datetime import datetime

# ANSI escape sequences for colored text and clearing the terminal
CLEAR_TERMINAL = "\033[H\033[J"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to save results to a file
def save_result(result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("results.txt", "a") as file:
        file.write(f"[{timestamp}] {result}\n")

# Main menu
def main_menu():
    while True:
        clear_terminal()
        print(f"{CYAN}Welcome to the Math Utility Program!{RESET}")
        print("1. Algebra")
        print("2. Complex Numbers")
        print("3. Other Utilities")
        print("4. View Saved Results")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            algebra_menu()
        elif choice == "2":
            complex_number_menu()
        elif choice == "3":
            other_utilities_menu()
        elif choice == "4":
            view_results()
        elif choice == "5":
            print(f"{YELLOW}Exiting the program. Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice! Please try again.{RESET}")
            input("Press Enter to continue...")

# Algebra menu
def algebra_menu():
    while True:
        clear_terminal()
        print(f"{BLUE}Algebra Menu{RESET}")
        print("1. Solve a Quadratic Equation")
        print("2. Arithmetic Progression")
        print("3. Simple Calculations")
        print("4. Exponentiation")
        print("5. Logarithms")
        print("6. Trigonometric Functions")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            solve_quadratic_equation()
        elif choice == "2":
            arithmetic_progression()
        elif choice == "3":
            simple_calculations()
        elif choice == "4":
            exponentiation()
        elif choice == "5":
            logarithms()
        elif choice == "6":
            trigonometric_functions()
        elif choice == "7":
            break
        else:
            print(f"{RED}Invalid choice! Please try again.{RESET}")
            input("Press Enter to continue...")

# Solve a quadratic equation
def solve_quadratic_equation():
    print(f"{GREEN}Solving a Quadratic Equation (ax^2 + bx + c = 0){RESET}")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            result = f"Roots are real and distinct: {root1}, {root2}"
        elif discriminant == 0:
            root = -b / (2*a)
            result = f"Root is real and repeated: {root}"
        else:
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
            result = f"Roots are complex: {root1}, {root2}"

        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid numbers.{RESET}")
    input("Press Enter to continue...")

# Arithmetic progression
def arithmetic_progression():
    print(f"{GREEN}Arithmetic Progression{RESET}")
    try:
        first_term = float(input("Enter the first term: "))
        common_difference = float(input("Enter the common difference: "))
        n = int(input("Enter the number of terms: "))

        sequence = [first_term + i * common_difference for i in range(n)]
        result = f"Arithmetic progression: {sequence}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid numbers.{RESET}")
    input("Press Enter to continue...")

# Simple calculations
def simple_calculations():
    print(f"{GREEN}Simple Calculations{RESET}")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == "+":
            result = f"{num1} + {num2} = {num1 + num2}"
        elif operation == "-":
            result = f"{num1} - {num2} = {num1 - num2}"
        elif operation == "*":
            result = f"{num1} * {num2} = {num1 * num2}"
        elif operation == "/":
            if num2 == 0:
                result = f"{RED}Error: Division by zero is not allowed.{RESET}"
            else:
                result = f"{num1} / {num2} = {num1 / num2}"
        else:
            result = f"{RED}Invalid operation! Please enter +, -, *, or /.{RESET}"

        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid numbers.{RESET}")
    input("Press Enter to continue...")

# Exponentiation
def exponentiation():
    print(f"{GREEN}Exponentiation{RESET}")
    try:
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = f"{base}^{exponent} = {base ** exponent}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid numbers.{RESET}")
    input("Press Enter to continue...")

# Logarithms
def logarithms():
    print(f"{GREEN}Logarithms{RESET}")
    try:
        number = float(input("Enter the number: "))
        base_input = input("Enter the base (use 10 for log base 10 or e for natural log): ")

        if base_input == "10":
            result = f"log10({number}) = {math.log10(number)}"
        elif base_input.lower() == "e":
            result = f"ln({number}) = {math.log(number)}"
        else:
            base = float(base_input)
            result = f"log({number}) with base {base} = {math.log(number, base)}"

        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid numbers.{RESET}")
    input("Press Enter to continue...")

# Trigonometric functions
def trigonometric_functions():
    print(f"{GREEN}Trigonometric Functions{RESET}")
    try:
        angle = float(input("Enter the angle in degrees: "))
        angle_rad = math.radians(angle)
        sin_val = math.sin(angle_rad)
        cos_val = math.cos(angle_rad)
        tan_val = math.tan(angle_rad)
        result = f"sin({angle}) = {sin_val}, cos({angle}) = {cos_val}, tan({angle}) = {tan_val}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter a valid number.{RESET}")
    input("Press Enter to continue...")

# Complex number menu
def complex_number_menu():
    while True:
        clear_terminal()
        print(f"{BLUE}Complex Numbers Menu{RESET}")
        print("1. Add Complex Numbers")
        print("2. Subtract Complex Numbers")
        print("3. Multiply Complex Numbers")
        print("4. Divide Complex Numbers")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_complex_numbers()
        elif choice == "2":
            subtract_complex_numbers()
        elif choice == "3":
            multiply_complex_numbers()
        elif choice == "4":
            divide_complex_numbers()
        elif choice == "5":
            break
        else:
            print(f"{RED}Invalid choice! Please try again.{RESET}")
            input("Press Enter to continue...")

# Add complex numbers
def add_complex_numbers():
    print(f"{GREEN}Adding Complex Numbers{RESET}")
    try:
        c1 = complex(input("Enter the first complex number (e.g., 1+2j): "))
        c2 = complex(input("Enter the second complex number (e.g., 3+4j): "))
        result = f"Sum: {c1 + c2}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid complex numbers.{RESET}")
    input("Press Enter to continue...")

# Subtract complex numbers
def subtract_complex_numbers():
    print(f"{GREEN}Subtracting Complex Numbers{RESET}")
    try:
        c1 = complex(input("Enter the first complex number (e.g., 1+2j): "))
        c2 = complex(input("Enter the second complex number (e.g., 3+4j): "))
        result = f"Difference: {c1 - c2}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid complex numbers.{RESET}")
    input("Press Enter to continue...")

# Multiply complex numbers
def multiply_complex_numbers():
    print(f"{GREEN}Multiplying Complex Numbers{RESET}")
    try:
        c1 = complex(input("Enter the first complex number (e.g., 1+2j): "))
        c2 = complex(input("Enter the second complex number (e.g., 3+4j): "))
        result = f"Product: {c1 * c2}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid complex numbers.{RESET}")
    input("Press Enter to continue...")

# Divide complex numbers
def divide_complex_numbers():
    print(f"{GREEN}Dividing Complex Numbers{RESET}")
    try:
        c1 = complex(input("Enter the first complex number (e.g., 1+2j): "))
        c2 = complex(input("Enter the second complex number (e.g., 3+4j): "))
        try:
            result = f"Quotient: {c1 / c2}"
        except ZeroDivisionError:
            result = f"{RED}Error: Division by zero is not allowed.{RESET}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid complex numbers.{RESET}")
    input("Press Enter to continue...")

# Generate a random number
def generate_random_number():
    print(f"{GREEN}Generate a Random Number{RESET}")
    try:
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        random_number = random.randint(lower_bound, upper_bound)
        result = f"Random number between {lower_bound} and {upper_bound}: {random_number}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid integers.{RESET}")
    input("Press Enter to continue...")

# Check if a string is a palindrome
def check_palindrome():
    print(f"{GREEN}Check Palindrome{RESET}")
    text = input("Enter a string: ")
    if text == text[::-1]:
        result = f"'{text}' is a palindrome."
    else:
        result = f"'{text}' is not a palindrome."
    print(result)
    save_result(result)
    input("Press Enter to continue...")

# Calculate the factorial of a number
def calculate_factorial():
    print(f"{GREEN}Calculate Factorial{RESET}")
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            result = f"{RED}Error: Factorial is not defined for negative numbers.{RESET}"
        else:
            factorial = math.factorial(number)
            result = f"{number}! = {factorial}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter a non-negative integer.{RESET}")
    input("Press Enter to continue...")

# Generate the Fibonacci sequence
def fibonacci_sequence():
    print(f"{GREEN}Fibonacci Sequence{RESET}")
    try:
        n = int(input("Enter the number of terms: "))
        if n <= 0:
            result = f"{RED}Error: Number of terms must be a positive integer.{RESET}"
        else:
            fib_sequence = []
            a, b = 0, 1
            for _ in range(n):
                fib_sequence.append(a)
                a, b = b, a + b
            result = f"Fibonacci sequence with {n} terms: {fib_sequence}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter a positive integer.{RESET}")
    input("Press Enter to continue...")

# Calculate GCD and LCM of two numbers
def gcd_and_lcm():
    print(f"{GREEN}GCD and LCM{RESET}")
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        gcd = math.gcd(num1, num2)
        lcm = abs(num1 * num2) // gcd if gcd != 0 else 0
        result = f"GCD of {num1} and {num2} is {gcd}, LCM is {lcm}"
        print(result)
        save_result(result)
    except ValueError:
        print(f"{RED}Invalid input! Please enter valid integers.{RESET}")
    input("Press Enter to continue...")

# Other utilities menu
def other_utilities_menu():
    while True:
        clear_terminal()
        print(f"{BLUE}Other Utilities Menu{RESET}")
        print("1. Generate a Random Number")
        print("2. Check Palindrome")
        print("3. Calculate Factorial")
        print("4. Fibonacci Sequence")
        print("5. GCD and LCM")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_random_number()
        elif choice == "2":
            check_palindrome()
        elif choice == "3":
            calculate_factorial()
        elif choice == "4":
            fibonacci_sequence()
        elif choice == "5":
            gcd_and_lcm()
        elif choice == "6":
            break
        else:
            print(f"{RED}Invalid choice! Please try again.{RESET}")
            input("Press Enter to continue...")

# View saved results
def view_results():
    print(f"{CYAN}Viewing Saved Results{RESET}")
    if os.path.exists("results.txt"):
        with open("results.txt", "r") as file:
            for line in file:
                print(line, end="")
    else:
        print(f"{YELLOW}No results found!{RESET}")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()