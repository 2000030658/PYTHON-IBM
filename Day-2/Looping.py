#looping -- for loop

'''for i in range(1,21):
    print(i)


#breakpoint keyword

for d in range(1,21):
    breakpoint()
    if d%5==0:
        break
    print(d)

#while loop 
a=0
while(a<21):
    print(a)
    a+=1'''



#looping in dict 


a1={
    '101':'abc',
    '102':'def',
    '103':'ghi',
    '104':'jkl'
}

for key,value in a1.items(): #here u can take any variable names insted of key,value like a,b
    print(key,value)