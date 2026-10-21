import random
import datetime

class Trip:
    def __init__(self, price_chart, vehicle_prices, promo_codes):
        self.price_chart = price_chart
        self.vehicle_prices = vehicle_prices
        self.promo_codes = promo_codes

    def get_trip_cost(self, source, destination, vehicle='trishaw'):
        # Implement method to calculate the trip cost based on the source, destination, and vehicle.
        source_index = self.get_city_index(source)
        destination_index = self.get_city_index(destination)
        cost = self.price_chart[source_index][destination_index]

        if vehicle == 'car':
            cost *= self.vehicle_prices['car']
        elif vehicle == 'van':
            cost *= self.vehicle_prices['van']

        return cost

    def get_city_index(self, city_name):
        cities = ['Alvin', 'Jamz', 'Razi', 'Mali', 'Zuhar']
        return cities.index(city_name)

    def apply_promo_code(self, total_cost, promo_code):
        # Implement method to apply the promo code deduction to the total cost.
        if promo_code in self.promo_codes:
            reduction = self.promo_codes[promo_code]
            total_cost -= reduction
        return total_cost

    def generate_random_promotion(self):
        # Implement method to generate a random promotion reduction if applicable.
        if random.randint(1, 10) == 1:  # 1 in 10 chance for random promotion
            return 5  # Fixed random promotion amount of 5 KMD
        return 0

    def save_invoice_to_file(self, invoice_details):
        # Implement method to save invoice details to a text file.
        with open("invoice.txt", "a") as file:
            file.write(invoice_details + "\n")

    def generate_invoice(self, source, destination, vehicle, promo_code):
        # Implement method to generate invoice details for a trip.
        trip_cost = self.get_trip_cost(source, destination, vehicle)
        promo_deduction = self.apply_promo_code(trip_cost, promo_code)
        random_promo_reduction = self.generate_random_promotion()

        final_cost = promo_deduction - random_promo_reduction

        date = datetime.datetime.now().strftime("%Y-%m-%d")
        time = datetime.datetime.now().strftime("%H:%M:%S")

        invoice_details = f"Date : {date}\nTime: {time}\nStart : {source}\nEnd : {destination}\n"
        invoice_details += f"Amount : {trip_cost} KMD\nPromo : {promo_deduction} KMD\n"
        invoice_details += f"Random Reduction : {random_promo_reduction} KMD\n"
        invoice_details += f"Final payment : {final_cost} KMD"

        self.save_invoice_to_file(invoice_details)

def main():
    price_chart = {
        'Alvin': [0, 20, 40, 40, 20],
        'Jamz': [20, 0, 20, 40, 40],
        'Razi': [40, 20, 0, 20, 40],
        'Mali': [40, 40, 20, 0, 20],
        'Zuhar': [20, 40, 40, 20, 0]
    }

    vehicle_prices = {
        'trishaw': 1,
        'car': 2,
        'van': 3
    }

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

    trip = Trip(price_chart, vehicle_prices, promo_codes)

    print("Welcome to DropMe™ - The Kingdom of Miranda's Cab Service")
    print("-------------------------------------------------------")
    print("Available commands:")
    print("1. dm <source_city> <destination_city> [vehicle]")
    print("2. dm <source_city> <destination_city> /pro<reduction_amount> [vehicle]")
    print("3. dm /price")
    print("4. dm <source_city> <destination_city> /c")
    print("5. dm <source_city> <destination_city> /v")
    print("6. dm /?")

    while True:
        command = input("Enter command: ")

        # Split the command only if it's not empty
        if command.strip():
            command_parts = command.split()

            if command_parts[0].lower() == 'dm':
                if len(command_parts) >= 3:
                    source_city = input("Enter source city: ")
                    destination_city = input("Enter destination city: ")
                    vehicle = input("Enter vehicle (trishaw, car, van): ").lower()
                    promo_code = None

                    if len(command_parts) >= 4:
                        if '/pro' in command_parts[3].lower():
                            promo_code = command_parts[3].lower().replace('/pro', '')
                            if len(command_parts) >= 5:
                                vehicle = command_parts[4].lower()
                        else:
                            vehicle = command_parts[3].lower()

                    trip.generate_invoice(source_city, destination_city, vehicle, promo_code)
                else:
                    print("Invalid command format. Type 'dm /?' for help.")
        else:
            print("Please enter a valid command.")

if __name__ == "__main__":
    main()
