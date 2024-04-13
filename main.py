# Arman Rafiee
# Jason Snytte

class Encode():
    def __init__(self, str):
        self.str = str
        self.num_list = []
        for i in self.str:
            self.num_list.append(int(i))
        


    def encode(self):
        encoded_str = ""
        for i in self.num_list:
            digit = i + 3
            if digit > 9:
                digit = digit - 10
            encoded_str += str(digit)
        self.str = encoded_str
        
        
class Decode:
    def __init__(self, string):
        self.str = string
        self.num_list = []
        for i in string:
            self.num_list.append(int(i))
    
    def decode(self):
        decoded_string = ""
        for i in self.num_list:
            digit = i - 3
            if digit < 0:
                digit += 10
            decoded_string += str(digit)
        self.str = decoded_string


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

        
        