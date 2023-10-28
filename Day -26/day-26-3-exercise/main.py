f1 = open("file1.txt") 
n1 = f1.readlines()
f2 = open("file2.txt")
n2 = f2.readlines()

result = [int(num) for num in n1 if num in n2 ]

# Write your code above 👆

print(result)


