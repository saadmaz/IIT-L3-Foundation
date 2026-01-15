fh = open("xyz.txt","r")
c = 0
while c<20:
    print(fh.read(1),end="")
    c +=1

fh.close()
