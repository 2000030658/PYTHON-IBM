#Single

print("Single Inheritance")
class Sample:
    def m1(self):
        print("m1")

class Demo(Sample):
    def m2(self):
        print("m2")

obj1 = Demo()
obj1.m1()
obj1.m2()


#Multi-level

print("Multi-Level Inheritance")
class Sample:
    def m1(self):
        print("m1")

class Demo(Sample):
    def m2(self):
        print("m2")

class Test(Demo):
    def m3(self):
        print("m3")

obj2=Test()
obj2.m1()
obj2.m2()
obj2.m3()


#Multiple

print("Multiple Inheritance")
class Sample:
    def m1(self):
        print("m1")

class Demo():
    def m2(self):
        print("m2")

class Test(Demo,Sample):
    def m3(self):
        print("m3")

obj3=Test()
obj3.m1()
obj3.m2()
obj3.m3()


#Hierarchical

print("Hierarchical Inheritance")
class Sample:
    def m1(self):
        print("m1")

class Demo(Sample):
    def m2(self):
        print("m2")

class Test(Sample):
    def m3(self):
        print("m3")

obj4=Demo()
obj5=Test()
obj4.m1()
obj4.m2()
obj5.m1()
obj5.m3()