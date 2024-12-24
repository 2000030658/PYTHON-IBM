a=int(input("Enter Value of a"))
b=int(input("Enter Value of b"))
try: 
    print(a/b)
except Exception:
    print("Division error")



class ExceptionError(Exception):
    def __init__(self,msg):
        super()

class Age:
    def test(self,age,per):
        if age<=17 or per<=60:
            raise ExceptionError("Not Eligible for registration")
        else:
            print("Registartion success")

obj = Age()
try:
    obj.test(17,56)
except Exception as e:
    print(e)