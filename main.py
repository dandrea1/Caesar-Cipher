import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
        end_text += char
    else:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
  print(f"Here's the {cipher_direction}d result: {end_text}")

def restart():
    user_restart = input("Do you want to start again? Type yes or no.\n")
    if user_restart == "yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            if direction == "encode" or direction == "decode":
                text = input("Type your message:\n").lower()
                shift = int(input("Type the shift number:\n"))
                caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
                restart()
            else:
                print("Sorry I didn't understand.")
                restart()
    elif user_restart == "no":
        print("Thanks for using the cipher.")
    else:
         print("Thanks for using the cipher.") 

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26  
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        restart()
    else:
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        restart()
else:
    print("Sorry I didn't understand.")
    restart()
    
