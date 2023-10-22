#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:

    names = names_file.readlines()
    
with open("./Input/Letters/starting_letter.txt") as letter:
    f_letter = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_f_letter = f_letter.replace(PLACEHOLDER, name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as output_file:
          output_file.write(new_f_letter)
        



#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp