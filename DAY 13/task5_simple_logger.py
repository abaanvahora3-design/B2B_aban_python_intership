import datetime

time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("log.txt", "a") as file:
    file.write(f"[{time_now}] User logged in\n")

with open("log.txt", "a") as file:
    file.write(f"[{time_now}] User performed action\n")

print("Logs written. Current logs:\n")

try:
    with open("log.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    pass