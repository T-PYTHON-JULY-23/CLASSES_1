class Panda():
    def __init__(self, species:str,age:int,wight:int,hight:int, fast_speed:int) -> None:
        self.__name = species
        self.__age = age
        self.__wight = wight
        self.__hight = hight
        self.__FastSpeed = fast_speed
    def eat(self):
        print(f"The {self.__name} eat bamboo shoots and leaves")
    def speed(self):
        print(f"The {self.__name} is {self.__age} years old, the hight is {self.__hight} and the wight is {self.__wight}")
        print(f"The {self.__name} the fast speed is : {self.__FastSpeed}")

    


panda1 = Panda("The gaint Panda",10,150,180,52)
panda1.eat()
panda1.speed()