bill = 0

def tip(value):
    tip = value * 0.1
    return tip

def JGB (value):
    tax = value * 0.15
    return tax

bill = int(input("Type bill amount : "))
print("Tip is :", tip(bill))
print("Tax is :", JGB(bill))
print("Final bill is :", bill + tip(bill) + JGB(bill))
