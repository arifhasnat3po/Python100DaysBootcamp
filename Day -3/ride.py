print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age in years? "))
bill = 0


if height > 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        bill += 5
        print(f"Please pay ${bill}.")
    elif age <= 18:
        bill += 7
        print(f"Please pay ${bill}.")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Please pay ${bill}.")
    else:
        bill += 12
        print(f"Please pay ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")

want_photo = input("Do you want a photo? Y or N.")
if want_photo == "Y":
    bill += 3
    print(f"Please pay ${bill}")
elif want_photo == "N":
    bill += 0
    print(f"Please pay ${bill}")