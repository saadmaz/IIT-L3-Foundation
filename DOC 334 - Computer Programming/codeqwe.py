import sys
import datetime

price_plan = {
    "Alvin": {"Alvin": 0, "Jamz": 20, "Razi": 40, "Mali": 40, "Zuhar": 20},
    "Jamz": {"Alvin": 20, "Jamz": 0, "Razi": 20, "Mali": 40, "Zuhar": 40},
    "Razi": {"Alvin": 40, "Jamz": 20, "Razi": 0, "Mali": 20, "Zuhar": 40},
    "Mali": {"Alvin": 40, "Jamz": 40, "Razi": 20, "Mali": 0, "Zuhar": 20},
    "Zuhar": {"Alvin": 20, "Jamz": 40, "Razi": 40, "Mali": 20, "Zuhar": 0},
}

vehicle_types = {"t": ("Trishaw", 1), "c": ("Car", 2), "v": ("Van", 3)}

promo_codes = {"pro2": ("2 KMD off", -2), "pro5": ("5% off", -0.05)}

def generate_invoice(source, destination, vehicle_type, promo_code):
    base_price = price_plan[source][destination]
    vehicle_name, vehicle_factor = vehicle_types[vehicle_type]
    final_price = base_price * vehicle_factor
    discount_amount = 0
    discount_description = ""
    if promo_code:
        discount_description, discount_amount = promo_codes[promo_code]
        if discount_amount < 0:
            discount_amount = final_price * discount_amount
        final_price += discount_amount
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = f"dm_{source}_{destination}_{date_time}.txt"
    with open(file_name, "w") as f:
        f.write(f"DropMe Invoice\n")
        f.write(f"Date and Time: {date_time}\n")
        f.write(f"Source: {source}\n")
        f.write(f"Destination: {destination}\n")
        f.write(f"Vehicle Type: {vehicle_name}\n")
        f.write(f"Base Price: {base_price} KMD\n")
        f.write(f"Vehicle Factor: {vehicle_factor}\n")
        f.write(f"Discount: {discount_description} ({discount_amount} KMD)\n")
        f.write(f"Final Price: {final_price} KMD\n")
        f.write(f"Thank you for choosing DropMe!\n")
    return file_name

if len(sys.argv) == 1:
    print("Usage: dm source destination [options]")
    print("Options:")
    print(" -t type (t for Trishaw (default), c for Car or v for Van)")
    print(" -p promo (pro2 or pro5)")
elif sys.argv[1] == "/price":
    for city in price_plan:
        print(city + "\t", end="")
        for price in price_plan[city].values():
            print(str(price) + "/" + str(price * 2) + "/" + str(price * 3) + "\t", end="")
        print()
else:
    source = sys.argv[1]
    destination = sys.argv[2]
    vehicle_type = sys.argv[3] if len(sys.argv) > 3 else "t"
    promo_code = sys.argv[4] if len(sys.argv) > 4 else None
    file_name = generate_invoice(source, destination, vehicle_type, promo_code)
    print(f"Invoice generated and saved to {file_name}")
