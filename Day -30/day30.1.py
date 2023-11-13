try:
    fruits = ["Apple", "Pear", "Orange"]

    def make_pie(index):
        fruit = fruits[index]
        print(fruit + "pie")

    make_pie(4)  # Applepie

except IndexError as e:
    print("Fruit Pie")
