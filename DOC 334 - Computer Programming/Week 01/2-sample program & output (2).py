# Create Variables
MyList = [100, 200, 550, 200, 150] 
List2 = ["hi", "how", "are", "you"]

#Some operations
print (MyList)
print (MyList[1:4])
print (len (MyList))

NewList = MyList + List2 # Join lists 
print (NewList)

NewList = MyList* 2 # Multiply lists
print (NewList)
print (111 in MyList) # Is 111 inside MyList

for Value in MyList: # Display all elements 
    print (Value)

print (MyList.count (200)) # How many times 200 occurs

print (MyList)
MyList.reverse () # Reversing elements 
print (MyList)

MyList.sort() # Sort ascending 
print (MyList)

MyList.sort(reverse=True) # Sort descending 
print (MyList)