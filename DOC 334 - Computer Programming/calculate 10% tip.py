import sys

bill = 0
tip = 0.10
JGB = 0.15
total_bill = 0

JGB = bill*JGB
tip = bill*tip
total_bill = bill+tip+JGB

bill = int(input("Type bill amount : "))

print (total_bill)
