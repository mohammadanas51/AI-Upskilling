a = (1,2,3,4,5,3)
print(type(a))
print(a)

b = (1,) # Comma to indicate that its a tuple 

# a[0] = 2 # Tuples are immutable 

# Tuple methods 

noOfOccurances = a.count(4) # Count the no of occurances of the element 4 
print(noOfOccurances)

index = a.index(3) # Returns the index of the element 3 - Returns the first occurance, wont give the index of subsequent occurances 
print(index)

print(len(a)) # Length of the tuple   