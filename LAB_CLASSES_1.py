class Panda:

    def __init__(self, name:str , fav_food:str, age:int, weight:int)->None:
        
        self.name = name 
        self.fav_food = fav_food 
        self.age= age 
        self.weight = weight

    def name_age(self):
        return f"Hello my name is {self.name} I'm a {self.age} year old panda"
    
    def food_Weight(self):
        return f"My favorite food are/is {self.fav_food} and I weight {self.weight}!"

    


panda1 =Panda("Bao","leaves",10,"350 lbs")
panda2 = Panda("Mei","bamboo",5,"150 lb")
panda3 =Panda("Basi","shoots",7,"276 lb")
panda4 = Panda("Pan","stems",20,"200 lb")

print(panda1.name_age())
print(panda1.food_Weight(),"\n")

print(panda2.name_age())
print(panda2.food_Weight(),"\n")


print(panda3.name_age())
print(panda3.food_Weight(),"\n")

print(panda4.name_age())
print(panda4.food_Weight(),"\n")



print(f"How old is {panda1.name}?")
print(panda1.age)

