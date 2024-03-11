# FIibonacci-Generator for CodeAlpha internship Task 1
This code defines a Python script to generate Fibonacci numbers and provides a user-friendly menu interface to interact with the Fibonacci generator.

- generate_fibonacci(limit): This function generates Fibonacci numbers up to the specified limit. It initializes a list fibonacci with the first two Fibonacci numbers [0, 1], and then iteratively calculates and appends the next Fibonacci numbers until the sum of the last two numbers exceeds the specified limit. The function returns the list of Fibonacci numbers.

- nth_fibonacci(n): This function efficiently finds the nth Fibonacci number. It uses a iterative approach to calculate the nth Fibonacci number by initializing two variables a and b to 0 and 1 respectively, and then iteratively updating them to calculate the nth Fibonacci number. It returns the nth Fibonacci number.

- is_fibonacci(num): This function checks if a given number is a Fibonacci number. It iteratively generates Fibonacci numbers until it finds a Fibonacci number greater than or equal to the given number. If the given number matches any of the generated Fibonacci numbers, it returns True, indicating that the number is a Fibonacci number; otherwise, it returns False.

- fibonacci_menu(): This function provides a user-friendly interface for interacting with the Fibonacci generator. It displays a menu with options to generate Fibonacci numbers, find the nth Fibonacci number, check if a number is Fibonacci, or exit the program. It takes user input to select an option and performs the corresponding operation based on the selected choice.

- The if __name__ == "__main__": block ensures that the fibonacci_menu() function is executed when the script is run directly.

The script can be run directly to access the Fibonacci generator through the command line interface. Users can choose options from the menu to perform various operations related to Fibonacci numbers
