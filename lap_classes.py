class Panda:
    def __init__(self, type:str , name:str, weight:int , age:int) -> None:
        self.type = type
        self.name = name
        self.weight = weight 
        self.age = age
        
    def about_panda(self):
        return f"The panda Type is {self.type} and the Name of the panda is: {self.name} and The height is: {self.weight}"
    def swim(self):
        return f"{self.name} is swimmimg"
    def climb_trees(self):
        return f"{self.name} climbs trees"
        
panda1 = Panda ("giant panda" , "Aliuropoda" , 90  , 11)
panda2 = Panda ("red panda" , "Ailurus fulgens" , 80 , 10)
panda3 = Panda ("giant panda" ," blue" , 90 ,9 )
panda4 = Panda ("red panda" , "lora" , 97 , 8)
print(panda1.about_panda())
print(panda4.name)
print(panda1.climb_trees())
print(panda3.swim())