# string slicing 
string = "Test" 
slicedString = string[0:3] # expected result - Te  -> Actual Result - Tes
print(slicedString)


string2 = "0123456789"
print(string2[1:7:3])


#String functions 

text = "flamingo"
lenth = len(text)

print(lenth)
print(text)
print(text.endswith("ingo"))
print(text.startswith("fla"))
print(text.capitalize())


string = "I am Flamingo the talking cat Meow"
newString = string.replace("cat", "lamb")

print(newString)