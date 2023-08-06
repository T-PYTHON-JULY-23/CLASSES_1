
class Panda:

    def __init__(self,PandaName:str,PandaAge:int,PandaSleepTime:str,PandaCaretaker:str):
        self.PandaName = PandaName
        self.PandaAge = PandaAge
        self.PandaSleepTime = PandaSleepTime
        self.PandaCaretaker = PandaCaretaker

    
    def PandaSchedule(self):
        
        print("Panda Schedule: \n")
        print (f"Panda {self.PandaName} Schedule: He sleep at {self.PandaSleepTime}, for more info. talk to his caretaker {self.PandaCaretaker}\n")

    
    def PrintInfo(self):

        print("Panda Info: \n")
        print (f"Panda name : {self.PandaName}\n")
        print (f"Panda age : {self.PandaAge}")


Panda1= Panda("lee",4,"5pm", "Ahmad Ai")
Panda2= Panda("may",2,'3pm', 'Abdullah Ai')
Panda3= Panda("bliy",6,'7pm', 'Ahmad Ai')
Panda4= Panda("summer",5,'8pm', 'Abdullah Ai') 

print("_"*30)
print("Instanc number 1:\n ")
print(f"Pand name: {Panda1.PandaName}\n")
Panda1.PandaSchedule()
Panda1.PrintInfo()
print("_"*30)

print("_"*30)
print("Instanc number 2:\n ")
print(f"Pand name: {Panda2.PandaName}\n")
Panda2.PandaSchedule()
Panda2.PrintInfo()
print("_"*30)

print("_"*30)
print("Instanc number 3:\n ")
print(f"Pand name: {Panda3.PandaName}\n")
Panda3.PandaSchedule()
Panda3.PrintInfo()
print("_"*30)

print("_"*30)
print("Instanc number 4:\n ")
print(f"Pand name: {Panda4.PandaName}\n")
Panda4.PandaSchedule()
Panda4.PrintInfo()
print("_"*30)