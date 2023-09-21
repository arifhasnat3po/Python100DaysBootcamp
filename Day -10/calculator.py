from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

# operations["*"]
num1 = int(input("What's the first number?: "))
# num2 = int(input("What's the second number?: "))

for i in operations:
  print(i)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

calculation = operations[operation_symbol]
answer = calculation(num1,num2)

# print(test)
print(f"{num1} {operation_symbol} {num2} = {answer}")
