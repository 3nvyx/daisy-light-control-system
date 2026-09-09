import requests
# Imports the 'requests' library (third-party installed with pip inside env) so we can send HTTP requests from Python.

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
# Sends an HTTP GET request to that URL.
# The server sends back a Response object, which we store in the variable "response".
# This object holds the status code, headers, and the raw body of the reply.

if response.status_code == 200:
    # response.status_code is a number the server sends back to say what happened.
    # 200 means "OK / success". Common others: 404 = not found, 500 = server error.
    data = response.json()
    # response.json() takes the raw text body (which is JSON — a text format)
    # and converts it into a Python object you can actually use.
    # PokeAPI returns a JSON *object* (curly braces { } in JSON), 
    # which Python converts into a dict (dictionary) — NOT a list/array.
    # A dict is a collection of key: value pairs, like a lookup table.
    # e.g. data = {"name": "pikachu", "height": 4, "weight": 60, ...}
    print(data["name"])
    print(data["height"])
    print(data["weight"])
    # data["name"] looks up the value stored under the key "name" in the dict.
    # This is called "indexing" — but since it's a dict, you use the KEY (a string),
    # not a numeric position like you would with a list.
else:
    print(f"Request failed: {response.status_code}")
    # If status_code wasn't 200, print an error message instead.
    # The f"" is an f-string — it lets you insert a variable's value directly
    # into the string using {curly braces}.

