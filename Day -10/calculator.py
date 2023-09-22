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
def calculator():
# operations["*"]
  num1 = int(input("What's the first number?: "))
  # num2 = int(input("What's the second number?: "))
  
  for i in operations:
    print(i)
  
  
  operation_symbol = input("Pick an operation: ")
  num2 = int(input("What's the next number?: "))
  
  calculation = operations[operation_symbol]
  answer = calculation(num1,num2)
  
  # print(test)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  
  should_continue = True
  
  while should_continue:
    
  
    operation_symbol = input("Pick another operation: ")
    num3 = int(input("What's the next number?: "))
    calculation = operations[operation_symbol]
    second_answer = calculation(calculation(num1, num2), num3)
    print(f"{num1} {operation_symbol} {num2} = {second_answer}")
  
    if input(f"Type 'y' to continue with {answer}, or type 'n' to exit for new calculation :").lower() =='y':
      num1 = answer
  
    else:
      should_continue = False
      calculator()

calculator()
  
