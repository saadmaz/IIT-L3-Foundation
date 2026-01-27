# Replace with the actual file path
file_path = "MyText123.txt"  

with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        print(line_count)
