class Panda:
    def __init__(self, name, age, weight_kg, location) -> None:
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
        self.location = location

    def eat(self, kg):
        if isinstance(kg, int):
            self.weight_kg += kg
        else:
            raise ValueError("enter a number in kg")
    
    def changeLocation(self, newLocation):
        self.location = newLocation

    