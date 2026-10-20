class Trip:
    def __init__(self, source, destination, vehicle='trishaw'):
        self.source = source
        self.destination = destination
        self.vehicle = vehicle
        self.price_chart = {
            'Alvin': [0, 20, 40, 40, 20],
            'Jamz': [20, 0, 20, 40, 40],
            'Razi': [40, 20, 0, 20, 40],
            'Mali': [40, 40, 20, 0, 20],
            'Zuhar': [20, 40, 40, 20, 0]
        }
        self.vehicle_prices = {
            'trishaw': 1,
            'car': 2,
            'van': 3
        }

    def get_trip_cost(self):
        source_index = self.get_city_index(self.source)
        destination_index = self.get_city_index(self.destination)
        cost = self.price_chart[source_index][destination_index]

        if self.vehicle == 'car':
            cost *= self.vehicle_prices['car']
        elif self.vehicle == 'van':
            cost *= self.vehicle_prices['van']

        return cost

    def get_city_index(self, city_name):
        cities = ['Alvin', 'Jamz', 'Razi', 'Mali', 'Zuhar']
        return cities.index(city_name)

    def generate_invoice(self):
        trip_cost = self.get_trip_cost()
        print("Invoice")
        print("-------")
        print(f"From: {self.source}")
        print(f"To: {self.destination}")
        print(f"Vehicle: {self.vehicle.capitalize()}")
        print(f"Trip Cost: {trip_cost} KMD")
        print("Thank you for using DropMe™!")


def main():
    print("Welcome to DropMe™ - The Kingdom of Miranda's Cab Service")
    print("-------------------------------------------------------")
    print("Available commands:")
    print("1. view_trip_details <source_city> <destination_city> [vehicle]")
    print("2. generate_invoice <source_city> <destination_city> [vehicle]")
    print("3. exit")

    while True:
        command = input("Enter command: ")
        command_parts = command.split()

        if command_parts[0] == 'view_trip_details':
            if len(command_parts) >= 3:
                source_city = command_parts[1]
                destination_city = command_parts[2]
                vehicle = 'trishaw'
                if len(command_parts) >= 4:
                    vehicle = command_parts[3]

                trip = Trip(source_city, destination_city, vehicle)
                trip_cost = trip.get_trip_cost()
                print(f"Trip details: {source_city} to {destination_city} using {vehicle.capitalize()}")
                print(f"Trip cost: {trip_cost} KMD")
            else:
                print("Invalid command format. Usage: view_trip_details <source_city> <destination_city> [vehicle]")

        elif command_parts[0] == 'generate_invoice':
            if len(command_parts) >= 3:
                source_city = command_parts[1]
                destination_city = command_parts[2]
                vehicle = 'trishaw'
                if len(command_parts) >= 4:
                    vehicle = command_parts[3]

                trip = Trip(source_city, destination_city, vehicle)
                trip.generate_invoice()
            else:
                print("Invalid command format. Usage: generate_invoice <source_city> <destination_city> [vehicle]")

        elif command_parts[0] == 'exit':
            print("Thank you for using DropMe™. Have a great day!")
            break

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
