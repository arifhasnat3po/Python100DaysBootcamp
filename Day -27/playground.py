def add(*number):
    print(number)
    sum = 0
    for i in number:
        sum += i

    return sum


print(add(3, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.model = kwargs.get("model")


# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")
print(my_car.model)
print(my_car.make)
