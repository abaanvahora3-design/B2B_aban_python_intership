with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

print("Even numbers found in the file:")
with open("numbers.txt", "r") as file:
    for line in file:
        num = int(line.strip()) 
        if num % 2 == 0:
            print(num)