import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

with open("response.json", "w") as file:
    file.write(response.text)

print("Response saved to response.json")