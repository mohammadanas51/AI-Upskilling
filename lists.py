# Trying out the list methods mentioned in the Python Handbook by CodeWithHarry

someList = [7,9,"harry"]

#list slicing - 0th element and 1st Element (2nd index excluded)
# print(someList[0:2])

numreicList = [4,5,7,9,1]
numreicList.sort()
print(numreicList)

numreicList.reverse()
print(numreicList)

numreicList.append(8)
print(numreicList)

numreicList.insert(3,8) # 8 inserted at 3rd index
print(numreicList)

numreicList.pop(2) # Delete element at index 2 
print(numreicList)

numreicList.remove(9) # Remove 9 from the list
print(numreicList)