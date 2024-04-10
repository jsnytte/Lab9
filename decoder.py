# Arman Rafiee
# Jason Snytte


class Decode:
    def __init__(self, string):
        self.num_list = []
        for i in string:
            self.num_list.append(int(i))
        # self.num_list = all the digits as there own number in a list
    
    def decode(self):
        decoded_string = ""
        for i in self.num_list:
            digit = i - 3
            if digit < 0:
                digit += 10
            decoded_string += digit
        return decoded_string