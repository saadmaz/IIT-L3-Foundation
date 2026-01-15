import sys
from datetime import datetime
import random
import math

# Cities price list for traveling
cities_price_list = {
    'Alvin': {'Alvin': 0, 'Jamz': 20, 'Razi': 40, 'Mali': 40, 'Zuhar': 20},
    'Jamz': {'Alvin': 20, 'Jamz': 0, 'Razi': 20, 'Mali': 40, 'Zuhar': 40},
    'Razi': {'Alvin': 40, 'Jamz': 20, 'Razi': 0, 'Mali': 20, 'Zuhar': 40},
    'Mali': {'Alvin': 40, 'Jamz': 40, 'Razi': 20, 'Mali': 0, 'Zuhar': 20},
    'Zuhar': {'Alvin': 20, 'Jamz': 40, 'Razi': 40, 'Mali': 20, 'Zuhar': 0}
}

# Transport modes
vehicle_prices = {
    'trishaw': 1,
    'car': 2,
    'van': 3
}

# Promotional codes
promo_codes = {
    'pro1': 1,
    'pro2': 2,
    'pro3': 3,
    'pro4': 4,
    'pro5': 5,
    'pro6': 6,
    'pro7': 7,
    'pro8': 8,
    'pro9': 9,
    'pro10': 10,
    'pro11': 11,
    'pro12': 12,
    'pro13': 13,
    'pro14': 14,
    'pro15': 15
}

# Defined transport service
def transport_service():
    while True:
        city_name = ['Alvin', 'Jamz', 'Razi', 'Mali', 'Zuhar']
        transport_mode = ['Trishaw', 'Car', 'Van']

        # Welcome message
        print("------------------Welcome to DropMe Cab service------------------")
        print("The available cities :", city_name)
        print("Available transport modes :", transport_mode)

        # Get trip details from the user
        current_city, destination_city, transport_method = get_trip_details()

        # Calculate trip price
        prices = calculate_prices(transport_method, current_city, destination_city)
        print("The gross price for your trip is:", prices, "KMD")

        # Apply promos and calculate final payment
        promo_type, total = operate_promos(prices)
        print("Total payment :", total, "KMD")

        # Save trip details to a text file
        save_details(current_city, destination_city, prices, promo_type, total)

        # Ask user if they want to use the service again
        user_choice = input("Do you want to use the service again? (yes/no): ").lower()
        if user_choice != 'yes':
            break

# Define promotion codes
def operate_promos(total):
    # Ask if the user has a promotional code
    promo_status = input("Do you have a promo code? (yes/no): ").lower()

    if promo_status == "yes":
        promo = input("Enter promo code here: ")
        while promo not in promo_codes:
            promo = input("Invalid promo code. Enter a valid promo code: ")

        # Apply promo code and calculate total payment
        discount = promo_codes[promo]
        total = max(total - discount, 0)
        return "promo", total
    else:
        # Randomly apply a 5 KMD discount with a 33.33% chance
        if random.randint(1, 3) == 1:
            total = max(total - 5, 0)
            return "random", total
        return "none", total
    
# Defined function to get the trip details
def get_trip_details():
    current_city = input("Enter the Start Location: ")
    destination_city = input("Enter the End Location: ")
    transport_method = input("Enter the transport mode (Trishaw/Car/Van): ").lower()

    # Ensure valid transport method is selected
    while transport_method not in vehicle_prices:
        transport_method = input("Invalid transport method. Enter a valid method (Trishaw/Car/Van): ").lower()

    return current_city, destination_city, transport_method

# Defined function to calculate prices based on the selected transport method
def calculate_prices(transport_method, current_city, destination_city):
    price = cities_price_list[current_city][destination_city]
    return price * vehicle_prices[transport_method]

# Defined function to save trip details to a text file
def save_details(departure, destination, prices, promo_type, total):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H_%M_%S")
    random_number = random.randint(1000, 9999)
    file_name = f"{date_time}_{random_number}.txt"

    with open(file_name, "w") as file:
        file.write(f"Date: {now.date()}\n")
        file.write(f"Time: {now.time()}\n")
        file.write(f"Start: {departure}\n")
        file.write(f"End: {destination}\n")
        file.write(f"Amount: {prices} KMD\n\n")
        file.write(f"Promo: {prices - total if promo_type == 'promo' else 0} KMD\n")
        file.write(f"Random Reduction: {prices - total if promo_type == 'random' else 0} KMD\n")
        file.write(f"Final payment: {total} KMD\n")
        

    print("\n------Receipt successfully printed------")
    print("Receipt name:", file_name)
    print("\n")

# Run the transport service
if __name__ == "__main__":
    transport_service()
