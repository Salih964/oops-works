class Employee:
    empcode:str
    name:str
    dept:str
    salary:int
    

    def __init__(self,code,name,dept,sal):
        self.empcode=code
        self.name=name
        self.dept=dept
        self.salary=sal

    def display(self):
        print(self.name,self.empcode,self.dept,)

obj1=Employee("0A34402","salih","Bca",20000)
obj1.display()

obj2=Employee("0B40802","rahul","b.com",30000 )
obj2.display()
      
