fh = open("num.txt","r")
c = 0
while c<6:
    num = int(fh.read(1))
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

    c += 1
fh.close()
