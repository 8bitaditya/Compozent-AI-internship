import requests

# Fetching data from jsonplaceholder API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    
    users = response.json()
    
    # Loop through each user and display their name, email, and address
    for user in users:
        name = user['name']
        email = user['email']
        address = user['address']
        street = address['street']
        city = address['city']
        
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Address: {street}, {city}")
        print("-" * 50)
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
