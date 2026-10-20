#import

import sys
from datetime import datetime
import random
import math

#defined materials

#defined transport service

def transport_service():
    city = ['Alvin','Jamz','Razi','Mali','Zuhar']
    transport_way = ['Trishaw','Car','Van']

    print("Welcome to the DropMe Cab service ")
    print("Available cities are; ", city)
    print("Available transport ways are; ", transport_way)

    current_city, the_city_you_go, transport_mod = distances()
    prices = calculate_prices(transport_mod,current_city,the_city_you_go)
    print("your price is, KMD ", prices)
    total, promo_type = operate_promos(prices)
    print("total", total)
    save_details(current_city, the_city_you_go,prices,promo_type,total)

#defined promocodes   

def operate_promos( total ):
    promo_status = ""
    while not (promo_status == "yes" or promo_status == "no"):
        promo_status = input("Do you have promo code? (yes/no) :")

    if (promo_status == "yes"):
        promo = input("Enter promo code here :")
        discount = int(promo[3:])
        print("discount", discount)

        while not (promo[:3] == "PRO" and (discount < 16 and discount > 0)):
            promo = input("Enter promo code here :")
            discount = int(promo[3:])
            print("discount", discount)
        total = total - discount
        if total < 0 : total = 0
        return total,"promo"
    else:
        if random.randint(0,1) == 1 : total = total - 5
        return total,"random"

#defined your current city, destination and transport mod

def distances():

    current_city = input("Enter the current city you are in, ")
    the_city_you_go = input("Enter the another city you want to go, ")
    transport_mod = input("Enter the transport mod(Trishaw/Car/Van)")

    return current_city, the_city_you_go, transport_mod

#defined prices in variues categorise

def calculate_prices(vehicle_type,departure,destination):
    if(vehicle_type == "Trishaw"):
        return base_price_list[departure][destination]
    elif(vehicle_type == "Car"):
        return base_price_list[departure][destination]*2
    elif(vehicle_type == "Van"):
        return base_price_list[departure][destination]*3
    else:
        return 0
    
def save_details(departure,destination,prices,promotype,total):
    file_path = "date_time.txt"
    prev_data = []
    discount = prices - total
    try:
        with open(file_path, "r") as file:
            data = file.read().strip() 
            prev_data = [x for x in data.split(";") if len(str(x))> 5]
            file.close()

        current_bill = f'''\nDate: {datetime.now().date()},
Time: {datetime.now().time()},
Start: {departure},
End: {destination},
Amount: {prices},
Promo: {discount if promotype=="promo" else 0},
Random Reduction: {discount if promotype=="random" else 0},
Final payment: {total}'''
        prev_data.append(current_bill)

        with open(file_path, "w") as file:
            if len(prev_data) > 3:
                del prev_data[0]
            for row in prev_data:
                file.write(str(row)+';')
            file.close()
            
            

    except FileNotFoundError:
        with open(file_path, "w") as file:
            initial_content = ""
            file.write(initial_content)
            current_bill = f'''\nDate: {datetime.now().date()},
Time: {datetime.now().time()},
Start: {departure},
End: {destination},
Amount: {prices},
Promo: {discount if promotype=="promo" else 0},
Random Reduction: {discount if promotype=="random" else 0},
FInal payment: {total};'''
            file.write(current_bill)
            file.close()
            print(prev_data)

   

#main price list 

base_price_list = {
    'Alvin' : {'Alvin':0,'Jamz':20,'Razi':40,'Mali':40,'Zuhar':20},
    'Jamz' : {'Alvin':20,'Jamz':0,'Razi':20,'Mali':40,'Zuhar':40},
    'Razi' : {'Alvin':40,'Jamz':20,'Razi':0,'Mali':20,'Zuhar':40},
    'Mali' : {'Alvin':40,'Jamz':40,'Razi':20,'Mali':0,'Zuhar':20},
    'Zuhar' : {'Alvin':20,'Jamz':40,'Razi':40,'Mali':20,'Zuhar':0}
}

transport_service()
