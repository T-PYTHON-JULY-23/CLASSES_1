class panda:
    def __init__(self,name:str,sleep_hours:int,reproduction:str,country_of_ive:str) -> None:
      self.name = name
      self.sleep_hours = sleep_hours
      self.reproduction = reproduction
      self.country_of_live = country_of_ive

    def sleep_hours_panda(self):
       return f"the sleep hours of {self.name} is {self.sleep_hours}"

    def reproduction_panda(self):
       return f" the {self.name} breed {self.reproduction} in early winter."
    


panda1 = panda("Giant Panda","10 hours ","Once in a  year", "south central China" )
panda2 = panda("Red Panda","17 hours","Once in a  year", "Eastern Himalayas")
panda3 = panda("Roy","20 hours","Once in a year","Nepal" )
panda4 = panda("joo","12 hours","Once in a year","Bhutan")

print("the name is: " , panda1.name)
print("the country of live is: " , panda2.country_of_live)

print(panda1.sleep_hours_panda())
print(panda2.sleep_hours_panda())
