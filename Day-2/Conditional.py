'''

#if 

a=int(input("Enter A value"))
b=int(input("Enter B value"))
if a==b:
    print("Equals")


#if else

if a>b:
    print("A is greater")
else:
    print("B is greater")


#else-if

if a>b:
    print("A is greater")
elif b>a:
    print("B is greater")
elif a==b:
    print("A and B are equal")
'''

#nested if

username = "asrith"
password = "myname1"

if(username == "asritha"):
    if(password == 'myname'):
        print("Login Success")
    else:
        print("Invalid Password")
else:
    print("Ivalid username")