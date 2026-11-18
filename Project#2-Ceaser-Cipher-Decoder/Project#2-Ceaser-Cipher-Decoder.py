

from secrets import choice

alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
## creates a LIST/ARRAY OF all letters in the alphabet

print("=================================")
print("  🔐  CAESAR CIPHER DECODER  🔐")
print("=================================")
print("  A B C D E  -->  D E F G H")
print("=================================")

match choice:
    case "1":
        print("Encrypt")
    case "2":
        print("Decrypt")
    case _:
        print("Invalid choice")

