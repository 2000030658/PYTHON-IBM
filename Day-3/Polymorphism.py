class Model1:
    def camera(self):
        print("40MP")
    def storage(self):
        print("126GB")

class Model2(Model1):
    def display(self):
        print("Curved Displey")
    def storage(self):
        print("256GB")
        #super().storage()


obj=Model2()
obj.camera()
obj.storage()