#Jason Snytte
#Arman Rafiee

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
            encoded_str += digit
        return encoded_str

