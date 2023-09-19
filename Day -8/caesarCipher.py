alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(cipher_direction, start_text, shift_amount):
  end_text = ""
  for letter in start_text:
    position = alphabet.index(letter)
    if cipher_direction=="encode":
      new_position = (position + shift_amount)%26
      end_text += alphabet[new_position]
      # print(f"The encoded text is {end_text}")
    elif cipher_direction == "decode":
      new_position = (position - shift_amount)%26
      end_text += alphabet[new_position]

  print(f"The {cipher_direction}d text is {end_text}")
  
caesar(cipher_direction=direction, start_text=text, shift_amount=shift)