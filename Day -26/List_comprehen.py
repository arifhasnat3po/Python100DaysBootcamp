numbers = [ 1,1,2,3,5,8,21,34,55]

squared_numbers = [item**2 for item in numbers]

print(squared_numbers)

result = [num for num in numbers if num%2==0]


print(result)