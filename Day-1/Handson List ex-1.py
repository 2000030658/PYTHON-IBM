a1=[]
print("1. Empty list created")

a=[34,56,90,42,"Welcome",87,21]
print("2. List created with more than 5 iteams")

b=len(a)
print("3. Length of the list",b) #length of the list

print("4(1). First item:",a[0]) #first item
print("4(2). Middle item:",a[b//2]) #middle item
print("4(3). Lat item:",a[-1]) #last item'''


mixed_data_types=["Asritha",21,5.3,"Unmarried","Andhra Pradesh"]
print("5. Declared a list with name mixed_data_types")

it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print("6. Declared companies list")

print("7. Companies List:",it_companies)
print("8. Length of companies list:",len(it_companies)) 

print("9(a). First Company in the list:",it_companies[0])
print("9(b). Middle Company in the list:",it_companies[len(it_companies)//2])
print("9(c). Last Company in the List:",it_companies[-1])

it_companies[5]='Capgemini'
print("10. List after modification of one company:",it_companies)

it_companies.append("Accenture")
print("11. List after addition of one company:",it_companies)

it_companies.insert((len(it_companies)//2),"Siemens")
print("12. List after insertion of company in the middle of list:",it_companies)

it_companies[4]=it_companies[4].upper()
print("13. One of the Uppercase company",it_companies)

res="#;".join(it_companies)
print("14. List after adding #; at the end:",res)

find="Google"
print("15. Check whether company present in the list: ",find in it_companies)

it_companies.sort()
print("16. Sorted List:",it_companies)

it_companies.reverse()
print("17. Reversed List:",it_companies)

slice_first=it_companies[:3]
print("18. Sliced out first 3 companies:",slice_first)

slice_last=it_companies[-3:]
print("19. Sliced out last 3 companies:",slice_last)

slice_middle=it_companies[len(it_companies)//2]
print("20. Sliced out middle company:",slice_middle)

it_companies.pop(0)
print("21. List After removal of first company:",it_companies)

it_companies.remove(it_companies[len(it_companies)//2])
print("22. List after removal of middle company:",it_companies)

it_companies.pop()
print("23. List after removal of last company:",it_companies)

it_companies.clear()
print("24. Removed all companies from the list: ",it_companies)

del it_companies
print("25. IT Companies list is destroyed")
#print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print("26. Concatination of two lists: ",front_end)

full_stack=front_end.copy()
print("Copied the joined the list")
index_redux=full_stack.index("Redux")
print("Found redux")
full_stack.insert(index_redux+1,"Python")
full_stack.insert(index_redux+2,"SQL")
print("27. List after adding python and sql after redux:",full_stack)