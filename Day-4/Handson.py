def add_two_numbers(a,b):
    return a+b

def area_of_circle(r):
    return 3,14*r*r

def add_all_nums(a): #a is list
    sum=0,i=0
    while(i<len(a)):
        sum+=a[i]
        i+=1
    return sum


def convert_celsius_to_fahrenheit(c):
    return (c*(9/5))+32

def check_season(month):
    if(month == 'Sep' or month == 'Oct' or month == 'Nov'):
        return ("Autumn")
    elif(month == 'Dec' or month == 'Jan' or month == 'Feb'):
        return ("Winter")
    elif(month == 'Mar' or month == 'April' or month == 'May'):
        return ("Spring")
    elif(month == 'June' or month == 'July' or month == 'Aug'):
        return "Summer"
    

