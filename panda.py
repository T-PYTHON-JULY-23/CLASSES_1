class Panda:
    def __init__(self,name:str,type:str,age:int,weight:float) -> None:
        self.__name =name
        self.__type = type
        self.__age = age
        self.__weight = weight
    def set_name(self, name:str):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("please input valid name")
    def set_type(self, type:str):
        if isinstance(type, str) and type.lower() == 'giant panda' or type.lower() =='red panda':
            self.__type = type
        else:
            raise ValueError("please input valid type")
    def set_age(self, age:int):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError("please input valid age")
    def set_weight(self, weight:float):
        if isinstance(weight, float):
            self.__weight = weight
        else:
            raise ValueError("please input valid weight") 
    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__type
    def get_age(self):
        return self.__age
    def get_weight(self):
        return self.__age
    def isHealthy(self):
        if self.__type == 'giant panda' and self.__weight >= 70 and self.__weight <= 120:
            return f'{self.__name} is Healthy'
        elif self.__type == 'red panda' and self.__weight >= 3.7 and self.__weight <= 6.2:
            return f'{self.__name} is Healthy'
        else:
            return f"{self.__name}'s weight is abnormal"
    def pandaInfo(self):
        return f'name: {self.__name}, age: {self.__age}, type: {self.__type}, weight: {self.__weight} status: {self.isHealthy()}'
#---------------------------------------------------------------
panda1 = Panda('dio','giant panda',3,78)
panda2 = Panda('mio','giant panda',7,60)
panda3 = Panda('aio','red panda',10,5)
panda4 = Panda('rio','red panda',4,10)
panda1.set_age(4)
print(panda1.get_type())
print(panda1.isHealthy())
print(panda2.isHealthy())
print(panda3.isHealthy())
print(panda4.isHealthy())
print('-'*20)
print(panda1.pandaInfo())
print(panda2.pandaInfo())
print(panda3.pandaInfo())
print(panda4.pandaInfo())