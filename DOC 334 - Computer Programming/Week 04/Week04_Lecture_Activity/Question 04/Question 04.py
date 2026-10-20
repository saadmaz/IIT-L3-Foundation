# Replace with the actual file path
file_path = "MyText123.txt"  

with open(file_path, 'r') as file:
        for line in file:
            numbers = line.split()
            odd_numbers = [num for num in numbers if int(num) % 2 == 1]
            print(' '.join(odd_numbers))
