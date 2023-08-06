class Panda:
    def __init__(self, name, age, weight, favorite_food):
        self.name = name
        self.age = age
        self.weight = weight
        self.favorite_food = favorite_food

    def eat(self):
        print(f"{self.name} is eating {self.favorite_food}.\n")

    def sleep(self):
        print(f"{self.name} is sleeping.\n")

    def Climbing(self):
        print(f"{self.name} is Climbing tree .\n")

# Create instances of the Panda class
panda1 = Panda("jeson", 5, 100, "bamboo")
panda2 = Panda("Grizz", 3, 80, "bamboo shoots")
panda3 = Panda("lena", 4, 90, "eucalyptus leaves")
panda4 = Panda("laly", 2, 70, "lotus roots")

# Print an attribute value
print(panda1.name)  # Output: jeson

# Call the two methods on each instance
panda1.eat()       
panda1.sleep()     
panda1.Climbing()

panda2.eat()       
panda2.sleep()     
panda2.Climbing()

panda3.eat()       
panda3.sleep()     
panda3.Climbing()

panda4.eat()       
panda4.sleep()   
panda4.Climbing()  