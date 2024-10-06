class student:
    name:str
    course:str
    degree:str

    def __init__(self,name,course, degree):
        self.name=name
        self.course=course
        self.degree=degree

    def display(self):
        print(self.name,self.course,self.degree)    

obj1=student("bijo","django","bca")

obj1.display()

obj2=student("salih","django","bca")

obj2.display()


# constructor?
# is aspecial method inside class
# constructor name always __init__(self)
# constructor invoked during object creation
# constructor(intializing instance varialble)[its the purpase of constructor]