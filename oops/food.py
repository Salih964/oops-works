class Food:

    name:str
    cusine:str
    meal_type:str

    def __init__(self,name,cusine,meal_type):
        self.name=name
        self.cusine=cusine
        self.meal_type=meal_type

    def display(self):
        print(self.name,self.cusine,self.meal_type)


obj1=Food("gheeroast","indian","breakfast")
obj1.display()




