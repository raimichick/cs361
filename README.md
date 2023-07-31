Quick guide:
1. install flask, re, json, requests
2. run service.py
3. service.py will show you the IP address you are currently on, and it will not change
4. start request.py

Detailed guide:
  You can install the above by using ```pip install <whatever>```. I am using VS Code and installed everything within the 
built-in terminal. Just make sure you are in the correct directory! Once that is complete, make a split terminal in VS Code. I go 
left to right, so in the left terminal, I started service.py. For me, I found I had better luck starting commands with
```sudo python3 service.py```. Once that is running, go to the other terminal and start request.py (again, I had better success with
```sudo python3 request.py```). You should immediately see a list of results from woodworkerssource.com fill up the right terminal
window.

# Example request:
```
import requests
import json

# Define the URL of the microservice
url = "http://localhost:3000/get_cost"

# Define the search criteria
search_criteria = {
    "criteria": "price"  # replace this with your actual search criteria
}

# Send a POST request to the microservice
response = requests.post(url, json=search_criteria)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the data
    print(json.dumps(data, indent=4))
else:
    print(f"Request failed with status code {response.status_code}.")
```
# The request section:

```
url = "http://localhost:3000/get_cost"

# Define the search criteria
search_criteria = {
    "criteria": "price"  # replace this with your actual search criteria
}

# Send a POST request to the microservice
response = requests.post(url, json=search_criteria)
```


# Check if the request was successful
```
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the data
    print(json.dumps(data, indent=4))
else:
    print(f"Request failed with status code {response.status_code}.")
```

# Files included: 
service.py - this is the microservice itself. It receives the request, reaches out to Woodworkers' Source,
             and returns the cost of the specified lumber if it finds it.

request.py - a simple example of how to utilize the microservice

![IMG_3039](https://github.com/raimichick/cs361/assets/101148339/e4a6ca47-68b6-46a8-9b5b-c25910f20d0c)

                                                                                    
