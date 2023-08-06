
class Panda:
    def __init__(self, species:str, speed:str, weight:int, food:str)->None:
        self.species = species
        self.speed = speed
        self.weight = weight
        self.food = food
    
    def eat(self):
        print(f"{self.species}  eating {self.food}!")
        
    
    def panda_speed(self):
        print(f"{self.species} have speed is {self.speed}.")
   
# Creating instances of the Panda class
panda1 = Panda(" Ailuropoda microta ", "slow", 100, "bamboo")
panda2 = Panda("Ailuropoda wulingshanensis ", "fast", 120, "apples")
panda3 = Panda(" Ailuropoda baconi", "slow", 160, "carrots")
panda4 = Panda("Ailuropoda melanoleuca", "medium", 140, "grapes")

# Accessing and printing an attribute value
print(panda1.species)

# Calling methods on each instance
panda1.eat()
panda1.panda_speed()

panda2.eat()
panda2.panda_speed()

panda3.eat()
panda3.panda_speed()

panda4.eat()
panda4.panda_speed()
