class GrandParent:

    def m1(self):
        print("grand parent m1 method")

class Parent(GrandParent):

    def m2(self):
        print("parent m2 method")    

class Child(Parent,GrandParent):
    print("child m method")   

    def m3(self):
        print("child m3 method")         



ch=Child()
ch.m3()
ch.m2()
ch.m1()