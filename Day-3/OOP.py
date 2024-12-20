class Test:
    a=10
    name = "python"

    def m1(self):  #self kewyword need to be used for every function in class
        print("M1 is called")

    def m2(self,a,b):
        print(a+b)
        self.m1() # use self keyword while we are calling a method in the same class

    def __init__(self):
        print("Constructor")


class Demo():
    b=90

obj1 = Test()
obj2 = Demo()
print(obj1.name)
obj1.m2(90,78) # m1(obj) 