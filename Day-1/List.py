'''a=int(input("Enter the value: "))
print(type(a))
b=input("Enter the value: ")
print(type(b))
print(id(a))
print(id(b))'''


#Collections

#list

a1=[1,4,67,'HI',89.7]
b1=[6,89.0,'Hello']
a1.append(23)
b1.insert(1,56)
a1[2] = 50
b1.remove("Hello")
a1.extend(b1)
print(a1)
print(b1)
a1.pop()
print(a1)