## Using what you learned about classes , create a class to represent a Panda.
#Q1

class Panda:


    def __init__(self, name:str, weight:int, species:str ,color:str) -> None:
        #adding attributes/properties
        self.name = name 
        self.weight = weight 
        self.species = species 
        self.color = color
        



    def eat(self):
         print ( f"{self.name} is sleeping ")


    def sleep(self):
        print(f"{self.name} is sleeping")

    def colors(self):
        print("it's color is: " f"{self.color}")


panda1 = Panda("meme", 90 , "mammals", "white and black")
panda2 = Panda("sara", 50, "mammals", "red")


print(panda1.color)

panda1.sleep()
panda1.eat()
panda1.colors()

panda2.sleep()
panda2.eat()
panda2.colors()


