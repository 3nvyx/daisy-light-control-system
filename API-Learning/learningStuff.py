import requests 

response = requests.get("https://pokeapi.co/api/v2/pokemon/sylveon")

if response.status_code == 200:

    data = response.json()
    print(" ")
    print("name is " + data["name"])
    print("height is " + str(data["height"]))
    print("weight is " + str(data["weight"]))
    print("order is " + str(data["order"]))
    print("id is " + str(data["id"]))
    print("types are " + str(data["types"]))
    print(" ")
else:
    print(f"Request failed: {response.status_code}")
   