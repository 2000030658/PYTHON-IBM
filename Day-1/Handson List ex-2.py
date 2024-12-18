ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("List is sorted")
print("1(a). Min age:",ages[0])
print("1(b). Max age:",ages[-1])

ages.append(ages[0])
ages.append(max(ages))
print("2. Min and max are affed to the list:",ages)

ages.sort()
median = (ages[len(ages)//2] + ages[(len(ages)//2)+1])/2
print("3. Median of the list:",median)

avg=sum(ages)
avg=avg/len(ages)
print("4. Average sum:",avg)

ran=max(ages)-min(ages)
print("5. Range of the ages:",ran)

print("6(a). Comparison of min & avg: ",abs(min(ages)-avg))
print("6(b). Comparison of max & avg: ",abs(max(ages)-avg))





countries=['China', 'Russia', 'USA', 'India', 'Sweden', 'Norway', 'Denmark']
print("Country list is created")
print("7. Middle country in the list:",countries[len(countries)//2])

mid=(len(countries)+1)//2
first_half=countries[:mid]
second_half=countries[mid:]
print("8(a). First Half:",first_half)
print("8(b). Second Half:",second_half)


scandic_countries=countries[-3:]
print("9. Scandic countries list:",scandic_countries)