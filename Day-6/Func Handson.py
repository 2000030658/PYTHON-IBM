'''def mul(N):
    return N*3

def div(N):
    if(N%7 == 0): return "True"
    else: return "False"

def avail(N):
    if N>=200 and N<=500: return "Yes"
    else: return "No"

print("Enter the Value of N ")
a=int(input())
print("1. Value after multiplying the number N with 3:",mul(a))
print("2. N divisible by 7:",div(a))
print("3. Does the number avaiable btw 200 and 500:",avail(a))


def get_discount(amount):
    if amount<500:
        return "Discount is 5%"
    elif amount>=500 and amount<2500:
        return "Discount is 10%"
    elif amount>=2500:
        return "Discount is 20%"
    
print("Enter bill amount")
bill=int(input())
print("4. Discount avail for the given amount:",get_discount(bill))


def show_number(n):
    print("5. Numbers from 0 to N with labels:\n")
    for i in range(0,n):
        if i==0: print(i,"- neither even nor odd")
        elif i%2 == 0: print(i,"- even")
        elif i%2 !=0: print(i,"- odd")

print("Enter the N value")
show_number(int(input()))

def perimeter_of_square(arg_1):
    return 4*arg_1

print("Enter side value")
side=int(input())
print("7. Perimeter of the square:",perimeter_of_square(side))

def calculate_percentage(number):
    if(number<1000):
        return "5%"
    else: return "10%"

print("Enter the number:")
number=int(input())
print("8. Return ",calculate_percentage(number)," of ",number)


def get_speed_status(speed):
    if speed<60: return "Normal"
    elif speed>=60 and speed<80: return "Warning"
    elif speed>=80: return "Over speed"

print("Enter speed")
speed=int(input())
print("9. Speed status:",get_speed_status(speed))

def count_of_uppercase(word):
    count=0
    for i in range(len(word)):
        if word[i] == word[i].upper():
            count+=1
    return count

print("Enter the string")
word=input()
print("10. Count of uppercase letters in given string:",count_of_uppercase(word))
'''

def valiadte_atm_pin_code(pin):
    count=0
    if len(pin)>=4 and len(pin)<6:
        for i in range(len(pin)):
            if pin[i].isnumeric():
                count+=1
        if count==len(pin): return "Valid Pin"
        else: return "Invalid Pin"
    else:
        return "Pin Length is either greater than 6 or less than 4"
    

print("Enter the pin")
pin=input()
print("11.",valiadte_atm_pin_code(pin))