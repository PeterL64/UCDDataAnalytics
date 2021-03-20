# Checking out the Wikipedia API
# Nested JSONs

# Import Packages
import requests

# Assign the URL to the variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# The variable pizza_extract holds the HTML of an extract from Wikipedia's Pizza page as a string.
# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
