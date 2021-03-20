# API Requests, Pulling movie data from OMDB, Open Movie Database
# Will query the API about the movie 'The Social Network'


# Import the requests package
import requests

# Assign to the variable url the URL of interest in order to query 'http://www.omdbapi.com' for
# the data corresponding to the movie The Social Network. The query string should have
# two arguments: apikey=72bc447a and t=the+social+network.
# You can combine them as follows: apikey=72bc447a&t=the+social+network
# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)
json_data = r.json()

# Print the text of the response object r by using its text attribute and
# passing the result to the print() function
print(r.text)
