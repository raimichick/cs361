"""
service.py contains all of the needed components for the microservice. Using this microservice, the user can
check to see if an item exists in the database (.csv file named database.csv). 
"""
from flask import Flask, request
from pandas import read_csv

app = Flask(__name__) 


# Define a route to handle incoming HTTP requests
@app.route('/', methods=['POST'])
def handle_request():
    # Retrieve the JSON data from the request body
    json_data = request.get_json()

    # Extract 'name' and 'csv_location' from the JSON data
    name = json_data.get('name')
    csv_location = json_data.get('csv_location')
    
    # search the database here. Change print statement and return to
    # something else
    data = read_csv(csv_location, encoding='latin-1')
    for i in data.iloc[:, 0]:
        if i == name:
            print("returning name")
            return name
    return "False"


if __name__ == '__main__':
    # Start the server
    app.run()