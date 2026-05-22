marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 23
}

print(marks, type(marks))
print(marks["Rohan"])

# Methods 
print("Items ", marks.items())

print("Keys ", marks.keys())

print("Values ", marks.values())

marks.update({"Harry" : 89, "New Student" : 45}) # Non existant values if passed will be updated 
print("Updated Marks ", marks)

print(marks.get("Rohan"))

#Sets 
# Empty Set 
emptySet = set() 

s = {1,5,5,5,4,6,7,1,"Flamingo"}
print(s) # Duplicate values will not be printed Also, order will not be maintained 

s.add(456)
print(s)

print("Length of this set ", len(s))

s.remove(1)
print("After removing 1 ", s)

s.remove("Flamingo")
print("After Removing Flamingo", s)

# Set union and intersection 
s1 = {1,45,4}
s2 = {7,8,9,6,1,4}
print("Union of two sets", s1.union(s2))  # Union combines both the sets without duplicate elements and in sorted order

print("Intersection of two sets", s1.intersection(s2)) # Intersection returns only the common values 