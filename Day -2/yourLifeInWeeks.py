# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#for 90 years of age

days_for_Years = 32850
weeks_for_Years = 4680
months_for_Years = 1080

age_days = int(age)*365
age_weeks = int(age)*52
age_months = int(age)*12

days_left = days_for_Years - age_days
weeks_left = weeks_for_Years - age_weeks
months_left = months_for_Years - age_months

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
# print(days_left)

# print(age_days)
# print(type(days_for_Years))

