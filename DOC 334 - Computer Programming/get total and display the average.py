fh = open("num.txt","r")
c = 0
total = 0
while c<6:
    num = int(fh.read(1))
    total += num
    c += 1
print("Total is",total)
print("Average is",total/6)
fh.close()
