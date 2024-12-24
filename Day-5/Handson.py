#1

a=input("Enter an integer ")
try:
    print("The square value is",int(a)*int(a))
except Exception:
    print("Entered input is not a valid format for an integer.")

#2

n=int(input("Enter the number of elements in the array"))
b=[]
print("Enter the elements in the array")
for i in range(n):
    try:
        b[i]=int(input())
    except Exception:
         print("NumberFormatError")
print("Enter the index of the array element you want to access")
c=int(input())
try:
    print(b[c])
except Exception:
    print("Index out of bounds")