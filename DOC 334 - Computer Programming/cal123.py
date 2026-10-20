val = 0
val2 = 0
add = 0
sub = 0
mul = 0
div = 0.0

def add(a,b):
    add = a + b
    return add

def sub(a,b):
    sub = a - b
    return sub

def mul(a,b):
    mul = a * b
    return mul
    
def div(a,b):
    div = a / b
    return div
    
val1 = int(input("Type value 1 : "))
val2 = int(input("Type value 1 : "))

ans = add(val1, val2)
print (ans)
  
ans = sub(val1, val2)
print (ans)

ans = mul(val1, val2)
print (ans)

ans = div(val1, val2)
print (ans)



