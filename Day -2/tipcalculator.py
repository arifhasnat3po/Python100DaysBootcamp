#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Tip Calculator\n")
bill = float(input("what was the total bill? $"))
tip = float(input("what percentage tip would you like to give? "))
split = int(input("How many people to split the bill? "))

percentip = float((100 + tip)/100)
print(percentip)

pay = (bill / split) * percentip
print("Each person should pay: $"+ "%.2f"% pay)
