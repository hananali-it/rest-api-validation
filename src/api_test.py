import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code:")
print(response.status_code)

print("\nResponse JSON:")
print(response.json())

data = response.json()

print("\nValidation Results:")

if response.status_code == 200:
    print("Status code is valid.")
else:
    print("Unexpected status code.")

if "userId" in data and "id" in data and "title" in data and "body" in data:
    print("Required fields are present.")
else:
    print("Missing required fields.")
