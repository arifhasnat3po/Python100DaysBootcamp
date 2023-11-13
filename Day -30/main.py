# File not found error
# with open("a_file.text") as f:
#     f.read()
try:
    file = open("a_file.text")
    a_dictionary = {"key": "value"}
    print(a_dictionary["dfsjgh"])

except FileNotFoundError:
    print("File not found.")
    file = open("a_file.text", "w")
except KeyError as error_message:
    print(f"Key Error.{error_message}")

else:
    content = file.read()
    print(content)
finally:
    # file.close()
    # print("File was close")
    # raise KeyError
    raise TypeError

# Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# Index Error

# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# Type error
# text = "abc"
# print(text + 5)
