import pandas as pd

# Use double backslashes or a raw string for the file path
data = pd.read_csv(
    r"C:\Users\ahpar\Documents\100daysofPython\Day -30\006 NATO-Phonetic-Alphabet-for-the-Code-Exercise\nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_data():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the alphabet please")
        generate_data()
    else:
        print(output_list)


generate_data()
