#TODO: Create a letter using starting_letter.txt
with open("./Input/Names/invited_names.txt") as names_file:

    names = names_file.read().splitlines()
    print(names)
with open("./Input/Letters/starting_letter.txt") as letter:
    f_letter = letter.read()
    print(f_letter)
personalized_messages = [f_letter.replace('[name]', name) for name in names]

with open("./Output/ReadyToSend/example.txt", "w") as output_file:
    for message in personalized_messages:
        output_file.write(message + '\n')
        



#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp