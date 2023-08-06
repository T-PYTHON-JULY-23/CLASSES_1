class Panda:

    def __init__(self, panda_name: str,  panda_type: str ,panda_age:int , panda_centry:str ) -> None:
        self.panda_type = panda_type
        self.panda_name =panda_name
        self.panda_age = panda_age
        self.panda_centry = panda_centry


    def sleep(self):
        return f"{self.panda_name} is sleeping"
    

    def eat(self):
         return f"{self.panda_name} is eating"


panda1 = Panda("jojo","Giant Panda", 35, "Mount Hamlaria")
panda2 = Panda("soso","Red Panda",  20, "Chinese")

print(panda1.panda_centry)
print(panda1.eat())
print(panda1.sleep())

print(panda2.panda_centry)
print(panda2.eat())
print(panda2.sleep())

