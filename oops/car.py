
class Vehicle:

    name:str
    brand:str

    def __init__(self,name,brand):
        self.name=name#fronx
        self.brand=brand#nexa

    def diplay_specs(self):
       print(self.name,self.brand)#fronx, nexa

class Car(Vehicle):

    transmission_type:str

    def __init__(self, name, brand, transmission):#("fronx", "nexa", "manuel")
        super().__init__(name,brand)#calling parent class constructor method
        self.transmission_type=transmission#manuel

    def diplay_specs(self):
        super().diplay_specs()
        print(self.transmission_type)#manuel



obj=Car("fronx","nexa","manuel")
obj.diplay_specs()