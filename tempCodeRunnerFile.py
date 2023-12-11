
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display menu options
print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4): ")


if choice == '1':
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

elif choice == '2':
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is: {result}")

elif choice == '3':
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")

elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The division of {num1} by {num2} is: {result}")
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid choice. Please enter a number between 1 and 4.")
