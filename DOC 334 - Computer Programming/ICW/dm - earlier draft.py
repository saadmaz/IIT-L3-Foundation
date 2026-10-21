import os
import datetime
import random

# Function to calculate the price between two cities for a given vehicle
def calculate_price(start_city, end_city, vehicle='trishaw'):
    # Price chart for all city combinations
    price_chart = {
        'Alvin': {'Alvin': 0, 'Jamz': 20, 'Razi': 40, 'Mali': 40, 'Zuhar': 20},
        'Jamz': {'Alvin': 20, 'Jamz': 0, 'Razi': 20, 'Mali': 40, 'Zuhar': 40},
        'Razi': {'Alvin': 40, 'Jamz': 20, 'Razi': 0, 'Mali': 20, 'Zuhar': 40},
        'Mali': {'Alvin': 40, 'Jamz': 40, 'Razi': 20, 'Mali': 0, 'Zuhar': 20},
        'Zuhar': {'Alvin': 20, 'Jamz': 40, 'Razi': 40, 'Mali': 20, 'Zuhar': 0},
    }

    # Select the appropriate price based on the vehicle
    if vehicle == 'trishaw':
        price = price_chart[start_city][end_city]
    elif vehicle == 'car':
        price = price_chart[start_city][end_city] * 2
    elif vehicle == 'van':
        price = price_chart[start_city][end_city] * 3
    else:
        raise ValueError("Invalid vehicle type. Use 'trishaw', 'car', or 'van'.")

    return price

# Function to generate a random reduction for lucky passengers
def generate_random_reduction():
    # The random reduction is always at a fixed price of 5 KMD
    return 5

# Function to generate the invoice and save it to a file
def generate_invoice(start_city, end_city, vehicle='trishaw', promo_code=0, random_reduction=0):
    # Get the current date and time for the invoice
    current_datetime = datetime.datetime.now()
    date_str = current_datetime.strftime('%Y-%m-%d')
    time_str = current_datetime.strftime('%H:%M:%S')

    # Calculate the price for the trip
    price = calculate_price(start_city, end_city, vehicle)

    # Apply the promo code and random reduction
    price -= promo_code
    price -= random_reduction

    # Prepare the invoice content
    invoice_content = f"Date : {date_str}\n"
    invoice_content += f"Time: {time_str}\n"
    invoice_content += f"Start : {start_city}\n"
    invoice_content += f"End : {end_city}\n"
    invoice_content += f"Amount : {price} KMD\n"
    invoice_content += f"Promo : {promo_code} KMD\n"
    invoice_content += f"Random Reduction : {random_reduction} KMD\n"
    invoice_content += f"Final payment : {price} KMD\n"

    # Save the invoice to a file with the proper name format
    file_name = current_datetime.strftime('%Y-%m-%d %H_%M_%S_%f') + '.txt'
    with open(file_name, 'w') as file:
        file.write(invoice_content)

    return invoice_content

# Function to handle the user commands
def handle_user_command(command):
    # Split the command and extract the components
    components = command.split()

    if len(components) == 2:
        if components[0] == 'dm':
            start_city = components[1]
            end_city = components[2]
            invoice = generate_invoice(start_city, end_city)
            print(invoice)
        elif components[0] == 'dm' and components[2] == '/price':
            # Show the full price plan for all vehicles
            # This will be a nested dictionary containing the prices for all city combinations
            price_chart = {
                'Alvin': {'Alvin': 0, 'Jamz': 20, 'Razi': 40, 'Mali': 40, 'Zuhar': 20},
                'Jamz': {'Alvin': 20, 'Jamz': 0, 'Razi': 20, 'Mali': 40, 'Zuhar': 40},
                'Razi': {'Alvin': 40, 'Jamz': 20, 'Razi': 0, 'Mali': 20, 'Zuhar': 40},
                'Mali': {'Alvin': 40, 'Jamz': 40, 'Razi': 20, 'Mali': 0, 'Zuhar': 20},
                'Zuhar': {'Alvin': 20, 'Jamz': 40, 'Razi': 40, 'Mali': 20, 'Zuhar': 0},
            }
            for city, prices in price_chart.items():
                print(f"{city}: {prices}")
        else:
            print("Invalid command. Type 'dm /?' to see available commands.")
    elif len(components) == 3:
        if components[0] == 'dm' and components[3] == '/c':
            # Generate invoice for a car ride
            start_city = components[1]
            end_city = components[2]
            invoice = generate_invoice(start_city, end_city, vehicle='car')
            print(invoice)
        elif components[0] == 'dm' and components[3] == '/v':
            # Generate invoice for a van ride
            start_city = components[1]
            end_city = components[2]
            invoice = generate_invoice(start_city, end_city, vehicle='van')
            print(invoice)
        else:
            print("Invalid command. Type 'dm /?' to see available commands.")
    elif len(components) == 4:
        if components[0] == 'dm':
            start_city = components[1]
            end_city = components[2]
            promo_code = int(components[3][4:])
            invoice = generate_invoice(start_city, end_city, promo_code=promo_code)
            print(invoice)
    elif len(components) == 5:
        if components[0] == 'dm':
            start_city = components[1]
            end_city = components[2]
            promo_code = int(components[3][4:])
            if components[4] == '/v':
                # Generate invoice for a van ride with promo code
                random_reduction = generate_random_reduction()
                invoice = generate_invoice(start_city, end_city, vehicle='van', promo_code=promo_code, random_reduction=random_reduction)
                print(invoice)
            elif components[4] == '/c':
                # Generate invoice for a car ride with promo code
                random_reduction = generate_random_reduction()
                invoice = generate_invoice(start_city, end_city, vehicle='car', promo_code=promo_code, random_reduction=random_reduction)
                print(invoice)
            else:
                print("Invalid command. Type 'dm /?' to see available commands.")
    else:
        print("Invalid command. Type 'dm /?' to see available commands.")

# Sample test cases
if __name__ == "__main__":
    # Test case 1
    handle_user_command('dm alvin razi')
    print("-------------")
    # Test case 2
    handle_user_command('dm alvin razi /pro2')
    print("-------------")
    # Test case 3
    handle_user_command('dm /price')
    print("-------------")
    # Test case 4
    handle_user_command('dm alvin razi /c')
    print("-------------")
    # Test case 5
    handle_user_command('dm alvin razi /pro10 /v')
