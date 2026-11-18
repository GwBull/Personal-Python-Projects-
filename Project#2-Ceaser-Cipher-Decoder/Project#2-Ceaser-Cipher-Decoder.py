


alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
## creates a LIST/ARRAY OF all letters in the alphabet

print("=================================")
print("  🔐  CAESAR CIPHER DECODER  🔐")
print("=================================")
print("  A B C D E  -->  D E F G H")
print("=================================")

choice = input("Would you like to encrypt or decrypt a message? (1 for encrypt, 2 for decrypt): ")
##prompt user for input to choose between encrypting or decrypting a message

answer = choice

match answer:
    case "1":
        print("Encrypt")
    case "2":
        print("Decrypt")
    case _:
        print("Invalid choice")

if answer == "1":
    message = input("Enter the message you want to encrypt: ")
elif answer == "2":
    message = input("Enter the message you want to decrypt: ")
else:
    print("Invalid choice. Please enter 1 for encrypt or 2 for decrypt.")

    result = ""
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + 3) 
            result = result + alphabet[new_position]
        else:
            result = result + char
    print(f"Encrypted message: {result}")
            


