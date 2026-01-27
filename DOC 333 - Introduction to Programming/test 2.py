import random
import datetime

price_chart = {
    "alvin": {"jamz": 20, "razi": 40, "mali": 40, "zuhar": 20},
    "jamz": {"alvin": 20, "razi": 20, "mali": 40, "zuhar": 40},
    "razi": {"alvin": 40, "jamz": 20, "mali": 20, "zuhar": 40},
    "mali": {"alvin": 40, "jamz": 40, "razi": 20, "zuhar": 20},
    "zuhar": {"alvin": 20, "jamz": 40, "razi": 40, "mali": 20}
}

def get_price(start_city, end_city):
    if start_city == end_city:
        return 0

    if start_city not in price_chart or end_city not in price_chart[start_city]:
        print("Invalid city names. Please enter valid city names.")
        return None

    return price_chart[start_city][end_city]

def get_promo(promo_code):
    if promo_code.startswith("pro") and promo_code[3:].isdigit():
        promo_amount = int(promo_code[3:])
        if 1 <= promo_amount <= 15:
            return promo_amount

    print("Sorry, this promo code is invalid")
    return 0

def generate_auto_promo():
    if random.random() < 0.2:
        return 5
    else:
        return 0

def generate_invoice(start_city, end_city, promo_code, vehicle):
    price = get_price(start_city, end_city)
    if price is None:
        return

    promo = get_promo(promo_code)

    if promo == 0:
        reduction = generate_auto_promo()
    else:
        reduction = 0

    total = price - promo - reduction

    vehicle_prices = {"trishaw": 1, "car": 2, "van": 3}
    if vehicle not in vehicle_prices:
        print("Sorry, this mode is not an option")
        return

    total *= vehicle_prices[vehicle]
    total_str = str(total) + " KMD"

    invoice = {
        "Date": str(datetime.datetime.now().strftime("%Y-%m-%d")),
        "Time": str(datetime.datetime.now().strftime("%H:%M:%S")),
        "Start": start_city.capitalize(),
        "End": end_city.capitalize(),
        "Amount": f"{price} KMD",
        "Promo": f"{promo} KMD",
        "Random Reduction": f"{reduction} KMD",
        "Final payment": total_str,
        "Vehicle": vehicle.capitalize()
    }

    filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{start_city}_{end_city}_{vehicle}.txt"
    with open(filename, "w") as file:
        for key, value in invoice.items():
            file.write(f"{key}: {value}\n")

    print(f"Invoice generated and saved as {filename}")

def handle_dm_command(args):
    if len(args) == 2:
        generate_invoice(args[0], args[1], "", "trishaw")
    elif len(args) == 3:
        if args[2].startswith("/pro"):
            generate_invoice(args[0], args[1], args[2][1:], "trishaw")  # Remove the forward slash before the promo code
        elif args[2] in ["/c", "/v"]:
            generate_invoice(args[0], args[1], "", args[2][1:])
        else:
            print("Invalid command format")
    elif len(args) == 4:
        if args[2].startswith("/pro") and args[3] in ["/c", "/v"]:
            generate_invoice(args[0], args[1], args[2][1:], args[3][1:])  # Remove the forward slashes before promo code and vehicle
        else:
            print("Invalid command format")
    else:
        print("Invalid command format")

def handle_price_command():
    for city, prices in price_chart.items():
        print(f"{city.capitalize()}: {prices}")

def handle_help_command():
    print("Command Types:")
    print("dm <start_city> <end_city>")
    print("dm <start_city> <end_city> /pro2|/pro5|/pro10")
    print("dm <start_city> <end_city> /c|/v")
    print("dm <start_city> <end_city> /pro2|/pro5|/pro10 /c|/v")

def main():
    while True:
        command = input("Enter command (or 'quit' to exit): ").strip().lower()
        if command == "quit":
            break

        args = command.split()
        if args[0] == "dm":
            handle_dm_command(args[1:])
        elif args[0] == "/price":
            handle_price_command()
        elif args[0] == "/?":
            handle_help_command()
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
