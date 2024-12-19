it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24]


#Exercises: Level 1

print("1. Length of the set it_companies:",len(it_companies))

it_companies.add("Twitter")
print("2. Twitter Company is added to the set")

it_companies.update(["Accenture",'Capgemini','Siemens'])
print("3. Set after addition of multiple companies",it_companies)

it_companies.remove("Accenture")
print("4. Set after removal of one company",it_companies)

print("5. Discard is used to remove the unsure item without raising the error, whereas for remove function it raises error if the iteam is not present in the set")


#Exericises: Level 2

print("1. Set A and B are joined",A|B)

print("2. A intersection B",A.intersection(B))

print("3. Is A sunset of B:",A.issubset(B))

print("4. Are A and B disjoint sets:",A.isdisjoint(B))

r1=A|B
r2=B|A
res=r1.union(r2)
print("5. Join A with B and B with A",res)

print("6. Symmetric differenec bwetween A and B",A.symmetric_difference(B))

del A
del B
print("7. A and B sets are deleted")


#Exericises: Level 3

agesset=set(age)
listlen=len(age)
setlen=len(agesset)
print("Size of List and Set",listlen,setlen)

print(agesset)