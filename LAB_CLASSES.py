

class Panda:
    def __init__(self,name:str,gender:str,color:str,voice:str) -> None:

        self.name=name
        self.gender=gender
        self.color=color
        self.voice=voice
        


    def pandaFeeling (self,voice):

        if voice == "Gee-Gee" :
            print("The panda is hungry")

        elif voice == "Woo Woo" :
             print("The panda feels unhappy ")

        elif voice == "barks" :   
            print("The panda gets scared")


    def pandaWeight (self,gender):

        if gender == "male" :
            print("The weight of the panda is approximately 110 kilogram")

        elif gender == "female" :
             print("The weight of the panda is approximately 95 kilogram")



    def introduce(self):
        return f"The name of panda is: {self.name} and gender: {self.gender}its color: {self.color}  panda voice '{self.voice}'"
    



panda1 = Panda("bobo","male","black","Woo Woo")
panda2 = Panda("soso","male","white","barks")

print(panda1.name)
print(panda1.gender)
print(panda1.color)
print(panda1.voice)


panda1.pandaFeeling("Gee-Gee")
panda1.pandaWeight("female")
print(panda2.introduce())
