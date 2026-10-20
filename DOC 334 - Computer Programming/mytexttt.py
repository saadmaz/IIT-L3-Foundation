#Creating variables
fo = None
fo2 = None

#You have to have a file called
#MyText.txt with some text in the same folder

#Open a text file with

fo = open("MyText.txt","r")
print ("File Name :",fo.name)
print ("Which mode :",fo.mode)
print ("What is in it?\n===============")
print (fo.read())

#Accessing files in the sub folder
fo2 = open ("sub\\MyTextSub2.txt","r")
print ("\nwhat is in it?\n===============")
print (fo2.read())

fo.close()
fo2.close()
