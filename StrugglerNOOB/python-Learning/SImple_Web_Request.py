import requests

# URL to make the request to
url = "https://jsonplaceholder.typicode.com/todos/1"

# Sending the GET request
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Parsing the response as JSON
    data = response.json()
    print("Response JSON:", data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
