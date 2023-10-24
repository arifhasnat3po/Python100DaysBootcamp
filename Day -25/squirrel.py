# import pandas as pd

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# # Define the colors to count (use consistent capitalization)
# colors_to_count = ['Gray', 'Cinnamon', 'Black']

# # Check for missing values and replace them with an empty string
# data['Primary Fur Color'].fillna('', inplace=True)

# # Initialize a dictionary to store counts
# color_counts = {}

# # Count the occurrences of each color
# for color in colors_to_count:
#     count = len(data[data['Primary Fur Color'] == color])
#     color_counts[color] = count

# # Print the counts
# for color, count in color_counts.items():
#     print(color, ":", count)

# # Create a DataFrame from the dictionary
# color_counts_df = pd.DataFrame(list(color_counts.items()), columns=['Color', 'Count'])

# # Save the result to a new CSV file
# color_counts_df.to_csv('color_counts.csv', index=False)

import csv
import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels)
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)

df.to_csv('Squirrel_Colors.csv',index =True)


print(df)
