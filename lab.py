class Panda:
    def __init__(self, name, age, weight_kg, location) -> None:
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
        self.location = location

    def eat(self, kg):
        if isinstance(kg, int):
            self.weight_kg += kg
            print(f"ymy, {self.name} weight is {self.weight_kg} kg, I add {kg}kg")
        else:
            raise ValueError("enter a number in kg")
    
    def doSport(self, m):
        '''the panda will lose 1 kg every 20m of sport'''
        lose_kg = round(m/10)
        self.weight_kg -= lose_kg
        print(f"Good job {self.name} in {m}m of sport you lost {lose_kg} kg, your new weight {self.weight_kg} kg")



panda1 = Panda("john", 12, 175, "riyadh")
panda2 = Panda("koko", 33, 200, "riyadh")
panda3 = Panda("nono", 98, 100, "abha")
panda4 = Panda("lolo", 40, 230, "abha")

print(panda1.weight_kg)
panda1.eat(5)
panda1.doSport(10)

print(panda2.weight_kg)
panda2.eat(5)
panda2.doSport(400)

print(panda3.weight_kg)
panda3.eat(5)
panda3.doSport(140)

print(panda4.weight_kg)
panda4.eat(5)
panda4.doSport(210)
