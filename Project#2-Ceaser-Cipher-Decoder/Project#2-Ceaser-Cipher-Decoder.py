


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
    message = input("Enter the message you want to encrypt: ").upper()

    result = ""
        ## start with an empty string to store the result
    for char in message:
            ## loop thorough each character in the message
            if char in alphabet:
                ## check if the character is in the alphabet
                position = alphabet.index(char)
                ## find the index of the character in the alphabet a = 0 b=1 c= 3 etc
                new_position = (position + 3) 
                ## add 3 to the index to shift the character by 3 positions
                result = result + alphabet[new_position]
                ## add the new character to the result string
            else:
                result = result + char
                ### if the character is not in the alphabet, add it to the result string as is
    print(f"Encrypted message: {result}")
        ### print the final encrypted message

elif answer == "2":
    message = input("Enter the message you want to decrypt: ").upper()

    result = ""
    for char in message:
            ## loop thorough each character in the message
            if char in alphabet:
                ## check if the character is in the alphabet
                position = alphabet.index(char)
                ## find the index of the character in the alphabet a = 0 b=1 c= 3 etc
                new_position = (position - 3) 
                ## subtract 3 from the index to shift the character by 3 positions
                result = result + alphabet[new_position]
                ## add the new character to the result string
            else:
                result = result + char
                ### if the character is not in the alphabet, add it to the result string as is
    print(f"Decrypted message: {result}")
    ### print the final decrypted message

else:
    print("Invalid choice. Please enter 1 for encrypt or 2 for decrypt.")


  

