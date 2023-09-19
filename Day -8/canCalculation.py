#Write your code below this line 👇

import math






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works. 
def paint_calc(height,width,cover):
  # print(round(height * width)/cover)
  result = math.ceil((height * width)/cover)
  print(f"You'll need {result} cans of paint.")
  

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

