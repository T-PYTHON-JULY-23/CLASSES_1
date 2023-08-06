class Panda:
    def __init__(self, mass:float, gender:str,age:int,habitat:str,) -> None:
        self.mass=mass
        self.gender=gender
        self.age=age
        self.habitat=habitat
        pass

    def panda_habitat(self):
        return {self.habitat}
    
    def panda_food(self):
        if self.habitat=="Sichuan Province":
            food="different type of bamboo"
        if self.habitat=="San Diego Zoo":
            food="milk, eggs, ground meat"
        if self.habitat=="Zoo Atlanta":
            food="Apples and carrots"
        return food

Jia_Jia=Panda(70,"female",25,"Sichuan Province")
yang_yang=Panda(80.50,"male",20,"Zoo Atlanta" )
xiang_xiang=Panda(100.75,"female",30, "Sichuan Province")
gao_gao=Panda(120.3,"male",19,"San Diego Zoo")


print(f"Jia Jia gender: {Jia_Jia.gender}")
print(f"Jia Jia lives in: {Jia_Jia.panda_habitat()}\n")
print(f"Yang Yang lives in: {yang_yang.panda_habitat()}\n")
print(f"xiang xiang lives in: {xiang_xiang.panda_habitat()}\n")
print(f"gao gao lives in: {gao_gao.panda_habitat()}\n")
print("what is the gaint panda food?")
print(f"Jia Jia eats: {Jia_Jia.panda_food()}\n")
print(f"Yang Yang eats: {yang_yang.panda_food()}\n")
print(f"xiang xiang eats: {xiang_xiang.panda_food()}\n")
print(f"gao gao eats: {gao_gao.panda_food()}\n")
