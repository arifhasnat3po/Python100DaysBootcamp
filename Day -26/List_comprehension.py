numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(numbers)
print(new_list)

# >>> name = "Arif"
# >>> new_list = [ letter for letter in name]
# >>> print(new_list)
# ['A', 'r', 'i', 'f']


r = range(1,5)

double = [n*2 for n in r]
print(double)


names = [
    "Emma",
    "Liam",
    "Olivia",
    "Noah",
    "Ava",
    "Sophia",
    "Jackson",
    "Aiden",
    "Isabella",
    "Lucas",
    "Mia",
    "Sophia",
    "Ethan"]

short_names = [name for name in names if len(name) < 5]
print(short_names)


lcap_names = [name.upper() for name in names if len(name) > 5]
print(lcap_names)