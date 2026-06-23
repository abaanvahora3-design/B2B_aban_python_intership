import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    
    print("--- Top 5 Latest Headlines ---")
    
    for index, post in enumerate(posts[:5], start=1):
        print(f"{index}. {post['title'].title()}")
else:
    print("Failed to fetch news data.")