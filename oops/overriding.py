# inheritance(single,multilevel,multiple)

class GrandParent:
    def m1(self):
        print("inside Grandparent m1 method")

class Parent:
    def m1(self):
        print("inside parent m1 method")

class Child(Parent,GrandParent):

    pass

ch=Child()
ch.m1()

