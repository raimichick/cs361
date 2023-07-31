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
