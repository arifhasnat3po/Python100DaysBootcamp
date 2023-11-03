def add(*number):
    print(number)
    sum = 0
    for i in number:
        sum += i
    
    return sum



print(add(3,4,5))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add = 3 , multiply = 5)