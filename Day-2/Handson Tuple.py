#Exercises: Level 1

a=()
print("1. Empty tuple is created.")

sis=('emily','olivia','sophia','ava','jules')
bro=('james','jack','henry','william','ethan')
print("2. Sisters and brothers tuples are created.")

siblings=sis+bro
print("3. Brothers and sisters tuple are joined:",siblings)

print("4. No.of siblings:",len(siblings))

parents=('charlotte','oliver')
siblings=siblings+parents
family_members=siblings
print("5. Family members tuple:",family_members)


#Exercises: Level 2


print("1. Sibilings tuple:",siblings)
print("1. Parents tuple:",parents)

fruits=('apple','mango','orange','papaya','watermelon')
veg=('carrrot','beans','beatroot','brocolli','tomato')
animal_prod=('meat','milk','eggs')
food_stuff_tp=fruits+veg+animal_prod
print("2. Fruits,veg,animal products tuples are created and are joined to food_stuff_tp")

food_stuff_lt=list(food_stuff_tp)
print("3. Tuple is changed into list:",food_stuff_lt)

slice_middle=food_stuff_lt[len(food_stuff_lt)//2]
print("4. Sliced out middle item from the list/tuple:",slice_middle)

print("5(a). Sliced out first three items from the list:",food_stuff_lt[:3])
print("5(b). Sliced out last three items from the list:",food_stuff_lt[-3:])

del food_stuff_tp
print("6. Food tuple is deleted.")

nordic_countries = ('Denmark', 'India','Iceland', 'Norway', 'Sweden')
print("7(a). Estonia is a nordic country or not:",'Estonia' in nordic_countries)
print("7(b). Iceland is a nordic country or not:",'Iceland' in nordic_countries)