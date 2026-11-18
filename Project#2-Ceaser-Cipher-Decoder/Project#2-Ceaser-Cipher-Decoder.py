
logo = r"""
  _____                           
 / ____|                          
| |     __ _  ___  ___  __ _ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__|
| |___| (_| |  __/\__ \ (_| | |   
 \_____\__,_|\___||___/\__,_|_|   
  _____ _       _               
 / ____(_)     | |              
| |     _ _ __ | |__   ___ _ __ 
| |    | | '_ \| '_ \ / _ \ '__|
| |____| | |_) | | | |  __/ |   
 \_____|_| .__/|_| |_|\___|_|   
         | |                    
         |_|                    

   A B C D E  -->  D E F G H
"""
print(logo)

alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
## creates a LIST/ARRAY OF all letters in the alphabet

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
    shift = int(input("Enter the shift value (1-25): "))
    ## prompt user for input to enter the message they want to encrypt and the shift value
    result = ""
        ## start with an empty string to store the result
    for char in message:
            ## loop thorough each character in the message
            if char in alphabet:
                ## check if the character is in the alphabet
                position = alphabet.index(char)
                ## find the index of the character in the alphabet a = 0 b=1 c= 3 etc
                new_position = (position + shift) 
                ## add the shift value to the index to shift the character by the shift value
                result = result + alphabet[new_position]
                ## add the new character to the result string
            else:
                result = result + char
                ### if the character is not in the alphabet, add it to the result string as is
    print(f"Encrypted message: {result}")
        ### print the final encrypted message

elif answer == "2":
    message = input("Enter the message you want to decrypt: ").upper()
    shift = int(input("Enter the shift value (1-25): "))
    ## prompt user for input to enter the message they want to decrypt and the shift value
    result = ""

    for char in message:
            ## loop thorough each character in the message
            if char in alphabet:
                ## check if the character is in the alphabet
                position = alphabet.index(char)
                ## find the index of the character in the alphabet a = 0 b=1 c= 3 etc
                new_position = (position - shift) 
                ## subtract the shift value from the index to shift the character by the shift value
                result = result + alphabet[new_position]
                ## add the new character to the result string
            else:
                result = result + char
                ### if the character is not in the alphabet, add it to the result string as is
    print(f"Decrypted message: {result}")
    ### print the final decrypted message

else:
    print("Invalid choice. Please enter 1 for encrypt or 2 for decrypt.")


  

