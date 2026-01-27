# Replace with the actual file path
file_path = "MyText123.txt"  

with open(file_path, 'r') as file:
        for line in file:
            numbers = line.split()
            even_numbers = [num for num in numbers if int(num) % 2 == 0]
            print(' '.join(even_numbers))
