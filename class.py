class Panda:
    def __init__(self,name,jender ,weight,height):
        self.name=name
        self.jender=jender
        self.weight=weight
        self.height=height

    
    def birth(self,name_son):
       son={self.name:name_son}
       return son
   
    def eating(self,meals):
        #how much he eat evry day 
        eat={self.name :meals}
        return eat
    
panda1=Panda("rock","male","130","100")
panda2=Panda("cake","female","110","80")
panda3=Panda("loly","female","108","70")
panda3=Panda("light","male","160","120")

print(f"panda name {panda1.name}")
print(f"name of mother and his son is {panda2.birth('moon')}",)

print(f" panda and how much eat meals evry day  {panda1.eating(5)} ")