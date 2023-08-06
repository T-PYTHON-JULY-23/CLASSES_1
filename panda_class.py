
class Panda:
    def __init__(self, country:str ,weight:float, height:float, age:int) :
        self.country = country
        self.weight = weight
        self.height = height
        self.age = age
    
    
    def intro(self):
        return f" this panda is form {self.country} and  and his age is {self.age}" 
   
    def helth(self):
     return f" the panda the weight of this panda is {self.weight} Kg and the height is {self.height} cm "
 
panda1 = Panda("australia", 300 , 150 , 7)
panda2 = Panda("canada", 400 , 200 , 5)
panda3 = Panda("china", 350 , 180 , 9)


print(panda3.country)
print(panda2.age)
print(panda1.intro())
print(panda2.intro())
print(panda3.helth())
