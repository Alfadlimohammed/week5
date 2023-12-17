# Get user input for a number
user_number = int(input("Enter a number: "))

# Check if the user-entered number is divisible by 10
if user_number % 10 == 0:
    print(f"The number {user_number} is divisible by 10.")
else:
    print(f"The number {user_number} is not divisible by 10.")
if __name__ == '__main__':
    # total.py
    import sys

    count = len(sys.argv)
    total = 0

    while count > 1:
        count -= 1
        total += float(sys.argv[count])
    average = total / len(sys.argv)
    print("Total is", total)
    print("Average is", average)
if __name__ == '__main__':
    # total.py
    import sys

    if len(sys.argv):
        print("No arguments were provided. Please pass numeric values as arguments.")
    else:
        count = len(sys.argv)
        total = 0

        while count > 1:
            count -= 1
            total += float(sys.argv[count])
        average = total / len(sys.argv)
        print("Total is", total)
        print("Average is", average)
if __name__ == '__main__':
    import sys
    print("The import search path for this program is", sys.path)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        arguments = [float(arg) for arg in sys.argv[1:]]
        avg = average(arguments)
        print(f"The average is: {avg}")
    else:
        print("No command-line arguments provided.")