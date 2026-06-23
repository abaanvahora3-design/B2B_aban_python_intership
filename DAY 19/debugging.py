"""
def calculate_total(string_list)
    total = 0
    for item in string_list:
        try
            num = int(item)
            total + num
        except ValueError
            print(f"Skipping invalid item: {item}")
    
    return total

data = ["10", "20", "apple", "30"]
result = calculate_total(data)
print("Total Sum = " + result)
"""


def calculate_total(string_list): 
    total = 0
    for item in string_list:
        try: 
            num = int(item)
            total += num 
        except ValueError: 
            print(f"Skipping invalid item: {item}")
    
    return total

data = ["10", "20", "apple", "30"]
result = calculate_total(data)
print(f"Total Sum = {result}")