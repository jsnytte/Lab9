# Arman Rafiee
# Jason Snytte

from encoder import Encode
from decoder import Decode


while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    option = int(input("Please enter an option: "))

    if option == 1:
        password = input("Please enter your password to encode: ")
        encoder = Encode(password)
        encoder.encode()
        password = encoder.str
        print("Your password has been encoded and stored!\n")
    elif option == 2:
        decoder = Decode(password)
        decoder.decode()
        print(f"The encoded password is {password}, and the original password is {decoder.str}.\n")
    elif option == 3:
        break

        
        