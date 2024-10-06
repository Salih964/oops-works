class Animal:


    name:str
    animal_type:str


    def __init__(self,name,animal_type):
        self.name=name
        self.animal_type=animal_type


    def display_details(self):
        print(self.name,self.animal_type)


class Lion(Animal):
    sound:str
    def __init__(self,name,animal_type,sound):
        super().__init__(name,animal_type)
        self.sound=sound   

    def display_details(self):
        super().display_details()
        print(self.sound)          

class Elephant(Animal):
    sound:str
    def __init__(self,name,animal_type,sound):
        super().__init__(name,animal_type)
        self.sound=sound

    def display_details(self):
        super().display_details()
        print(self.sound)   


obj=Lion("lion","carnivore","roar")
obj.display_details()

obj1=Elephant("elephant","herbivora","rumble")
obj1.display_details()