class Panda():

    def __init__(self,hight:str,wight:float,name:str,age:int) -> None:
        self.hight=hight
        self.wight=wight
        self.name=name
        self.age=age
    

    def set_hight_wight(self,hight:float,wight:float):
        self.hight=hight
        self.wight=wight


    def panda_say_hello(self):
        
        print(f'Hello im {self.name}')
    

first_panda=Panda(166,75,'first',5)
secend_panda=Panda(200,90,'secend',7)
thired_panda=Panda(200,90,'3rd',7)
forth_panda=Panda(200,90,'forth',7)



print(first_panda.name,first_panda.age,first_panda.hight,first_panda.wight)
print(secend_panda.name,secend_panda.age,secend_panda.hight,secend_panda.wight)

first_panda.panda_say_hello()
secend_panda.panda_say_hello()
thired_panda.panda_say_hello()
forth_panda.panda_say_hello()


first_panda.set_hight_wight(secend_panda.hight,secend_panda.wight)

print(first_panda.name,first_panda.age,first_panda.hight,first_panda.wight)
