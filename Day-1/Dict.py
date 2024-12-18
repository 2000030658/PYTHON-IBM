a1={id:908,"name":"abc","sal":90000}
print(a1)
print(type(a1))
a1[id]=102
print(a1)
a1['loc'] = "bglr"
print(a1)


#nested dictionary

b1={
    101:"Java",
    102:"C++",
    103:{
        "Java": "Scanner",
        "Python" : "Numpy"
        }
    }

print(b1)
print(b1[101])
print(b1[103]["Python"]) #dimensinal indexing