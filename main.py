# Arman Rafiee
# Jason Snytte

from encoder import Encode
from decoder import Decode

while True:
    print("Menu",
    "-------------",
    "1. Encode",
    "2. Decode",
    "3. Quit")

    option = int(input("Please enter an option: "))

    if option == 1:
        str_to_encode = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
    elif option == 2: