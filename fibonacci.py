def generate_fibonacci(limit):
    """It will generate Fibonacci numbers up to the specified limit."""
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= limit:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci


def nth_fibonacci(n):
    """It will find the nth Fibonacci number efficiently."""
    if n < 0:
        raise ValueError("Invalid input: n must be a non-negative integer.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_fibonacci(num):
    """It will check if a given number is a Fibonacci number."""
    if num < 0:
        return False
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num


def fibonacci_menu():
    """It will provide a user-friendly interface(console) for interacting with the Fibonacci generator."""
    print("Welcome to the Fibonacci Generator!")
    while True:
        print("\nMenu:")
        print("1. Generate Fibonacci numbers up to a limit")
        print("2. Find the nth Fibonacci number")
        print("3. Check if a number is Fibonacci")
        print("4. Exit")
        choice = input("Please choose an option (1/2/3/4): ")

        if choice == '1':
            limit = int(input("Enter the limit: "))
            fibonacci_numbers = generate_fibonacci(limit)
            print(f"Fibonacci numbers up to {limit}: {fibonacci_numbers}")
        elif choice == '2':
            n = int(input("Enter the value of n: "))
            fibonacci_number = nth_fibonacci(n)
            print(f"The {n}th Fibonacci number is: {fibonacci_number}")
        elif choice == '3':
            num = int(input("Enter the number to check: "))
            if is_fibonacci(num):
                print(f"{num} is a Fibonacci number.")
            else:
                print(f"{num} is not a Fibonacci number.")
        elif choice == '4':
            print("Exiting the Fibonacci Generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    fibonacci_menu()
