class panda:
    def __init__(self,color:str,age:int, hight:int , Weight:int):
        self.color=color
        self.age= age
        self.hight=hight
        self.weight=Weight
        
    def devouring_bamboo(self,meals):
        return (f"this panda is {self.color}, devouring bamboo {meals} in day")   
    
    def sleep_hours(self,hours):
        return (f"this panda is {self.color}, sleep hours {hours} in day")   

panda1=panda("brown",20,180,113)
panda2=panda("white",5,90,100)
panda3=panda("black",10,120,105)
panda4=panda("white & black",26,180,120)

print(panda1.devouring_bamboo(5))
print(panda2.sleep_hours(10))
print(panda3.devouring_bamboo(3))
print(panda4.sleep_hours(9))


