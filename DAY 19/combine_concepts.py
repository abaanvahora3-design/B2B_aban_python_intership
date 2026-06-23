import requests
import json

def fetch_and_save_contacts():
    url = "https://jsonplaceholder.typicode.com/users"
    
    print("Fetching users from API...")
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            api_data = response.json()
            
            clean_contacts = []

            for user in api_data:
                clean_contact = {
                    "name": user["name"],
                    "email": user["email"]
                }
                clean_contacts.append(clean_contact)
                
            with open("contacts.json", "w") as file:
                json.dump(clean_contacts, file, indent=4)
                
            print(f"Successfully saved {len(clean_contacts)} contacts to contacts.json!")
            
        else:
            print(f"API Error. Status Code: {response.status_code}")
            
    except requests.exceptions.RequestException:
        print("Network Error: Could not connect to the API.")
        
fetch_and_save_contacts()
