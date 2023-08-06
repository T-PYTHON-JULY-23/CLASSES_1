class Panda :
    def __init__(self,weight : int , name : str, age : int , gender : str) -> None: #defined 4 atributes
        self.weight = weight
        self.name = name
        self.age = age
        self.gender = gender
    def eat_bamboo(self): #defined first fun
        print(f"{self.name} is eating bamboo.")

    def play(self):# defined second fun
        print(f"{self.name} is playing.")

#Create 4 instances of the class Panda
panda1=Panda(100,"mei mei",7,"female")
panda2 = Panda(150,"geigei",9,"male")
panda3 = Panda(137,"neinei",12,"male")
panda4= Panda(124,"roro",8,"female")
#print 1 attribute value
print(panda1.name)
#call the two methods on each instance. 
#1\
Panda.eat_bamboo(panda1)
Panda.eat_bamboo(panda2)
Panda.eat_bamboo(panda3)
Panda.eat_bamboo(panda4)
#2\
Panda.play(panda1)
Panda.play(panda2)
Panda.play(panda3)
Panda.play(panda4)



        