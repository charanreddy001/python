



def even_odd(number):
    " this is called doctype comment "
    if number % 2 == 0:
        print(" {} this is even".format(number))
    else:
        print(" {} this is odd number".format(number))

even_odd(90)
# this is used to read comment in def
print(even_odd.__doc__)


def squaring(number):
    square = number*number
    print("the square of {} is {} ".format(number, square))


squaring(9)
print(" ")
#                                             OOPS(object oriented programming language)


class phone:
    def __init__(self, model, rom, colour):
        self.model = model
        self.rom = rom
        self.colour = colour

    def info(self):
        print("model is :", self.model)
        print("rom is : ", self.rom)
        print("colour is : ", self.colour)


ph = phone("15pro max", "8GB", "cyan")
ph.info()


class IPhone:
    def __init__(self):
        self.model = " 15 pro max"
        self.ram = "8GB"
        self.colour = "white"

    def info(self):
        print('the model is:', self.model)
        print("the ram is : ", self.ram)
        print("the colour is : ", self.colour)


ph3 = IPhone()

ph3.info()
# any one can edit this like below
# but if you don't edit upp one will come
ph3.model = "16 pro max"
    

