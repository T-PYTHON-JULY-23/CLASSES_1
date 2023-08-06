class Panda:
    def __init__(self,age:int,weight : float, height:float,food:str):
        self.age = age
        self.weight = weight
        self.height = height
        self.food = food
    
    def display1(self):
        return f"This panda with age {self.age} years old and favirate food is {self.food} and"
    def display2(self):
        return f"with weight {self.weight} kg  and with height {self.height} cm"
    

p1 = Panda(20,125,1.3,"Bamboo")
p2 = Panda(23,130,1.5,"roots")
p3 = Panda(18,105,1.2,"stems")
p4 = Panda(27,110,1.4,"roots")

print(p1.display1(),p1.display2())
print(p2.display1(),p2.display2())
print(p3.display1(),p3.display2())
print(p4.display1(),p4.display2())
