import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

print("Status code:", response.status_code)
print("Response JSON:", response.json())