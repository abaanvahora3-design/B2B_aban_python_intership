import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    
    print("--- User Contact Cards ---\n")
    
    for user in users[:3]: 
        print(f"Name   : {user['name']}")
        print(f"Email  : {user['email']}")
        
        print(f"Company: {user['company']['name']}")
        print("-" * 30)

else:
    print("Failed to fetch data.")
