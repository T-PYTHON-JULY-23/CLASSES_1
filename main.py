class Panda:
    def __init__(self,name:str,age:int,weight : float, height:float,food:str):
        self.age = age
        self.weight = weight
        self.height = height
        self.food = food
        self.name = name
    
    def display1(self):
        return f"{self.name} age is {self.age} years old and favirate food is {self.food} and"
    def display2(self):
        return f"{self.name} weight is {self.weight} kg  and with height {self.height} cm"
    def sleep(self):
        return f"{self.name} is sleeping"
    def eat(self):
        self.weight += 7 #kg
        return f"{self.name} is eating {self.food}"
    

p1 = Panda("Alex",20,125,1.3,"Bamboo")
p2 = Panda("Bone",23,130,1.5,"Bamboo")
p3 = Panda("Lolo",18,105,1.2,"stems")
p4 = Panda("kavo",27,110,1.4,"roots")

print(p1.sleep())
print(p2.eat())
print(p3.sleep())
print(p4.eat())


print(p1.display1(),p1.display2())
print(p2.display1(),p2.display2())
print(p3.display1(),p3.display2())
print(p4.display1(),p4.display2())
