from flask import Flask, request, jsonify
import requests
import json
import re

app = Flask(__name__)

@app.route('/get_cost', methods=['POST'])
def get_cost():
    # Grab the search criteria from the request
    criteria = request.json['criteria']

    # Append it to the WoodworkersSource URL
    url = f"https://www.woodworkerssource.com/search.html?Search={criteria}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the entire HTML content
        html_content = response.text

        # Use regex to find the "items" list inside the script tag
        pattern = re.compile(r'"items": (\[.*?\])', re.DOTALL)
        matches = pattern.findall(html_content)

        if matches:
            # Get the first match (items_list) from the list of matches
            json_data = matches[0]

            # Parse the JSON data
            try:
                items_list = json.loads(json_data)

                # Now, you can work with the list of items as needed

                # Create a list to store the formatted items
                formatted_items = []
                for item in items_list:
                    # Add each item to the formatted list as a dictionary
                    formatted_item = {
                        "item_name": item["item_name"],
                        "price": item["price"],
                        "quantity": item["quantity"]
                        # Add more fields as needed
                    }
                    formatted_items.append(formatted_item)

                json_response = jsonify(formatted_items)

                # Return the JSON response
                return json_response

            except json.JSONDecodeError:
                print(f"Error: Encountered invalid JSON: {json_data}")
                return jsonify(error="Encountered invalid JSON"), 500
        else:
            print("Error: Could not find 'items' in HTML.")
            return jsonify(error="Could not find 'items' in HTML"), 500
    else:
        print("Failed to fetch the website content.")
        return jsonify(error="Failed to fetch the website content."), 500

if __name__ == '__main__':
    app.run(port=3000, debug=True)
