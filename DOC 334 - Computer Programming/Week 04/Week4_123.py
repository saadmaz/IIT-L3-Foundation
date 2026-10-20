#Creating Variables
fo = 0

#Open a text file with
fo = open ("MyTextLines.txt" , "r")
with fo:
    count = 1
    for line in fo:
        #reading line by line
        print ("line", count , "-" , line, end="")
        count += 1 
    
