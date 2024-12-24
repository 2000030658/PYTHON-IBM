from threading import Thread
from time import sleep

class Sample(Thread):
    def m1(self):
        for i in range(1,21):
            print(i)
            sleep(1)
    def run(self):
        self.m1()

class Demo(Thread):
    def m2(self):
        for i in range(21,41):
            print(i)
            sleep(1)
    def run(self):
        self.m2()

o1=Sample()
o2=Demo()
o1.start()
o2.start()
o1.join()
o2.join()
print("End")