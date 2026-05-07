import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url=url)
# print(dir(response))
#print(type(response.json()))

for key, value in response.json().items():
    if key == "userId":
        if value in [1,2,3,4]:
            print("User found")
        else:
            print("User not found")

            