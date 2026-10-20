#Creating Variables
fo = None

#Opening a text file
fo = open ("ReadThis.txt","r")

for x in range (3):
    print (fo.read(0),end="")

fo.close()    
