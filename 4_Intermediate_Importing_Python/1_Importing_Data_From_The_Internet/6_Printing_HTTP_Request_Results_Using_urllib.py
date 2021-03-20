# Printing HTTP request results using urllib

# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request
request = Request(url)

# Send the request and catch the response in the variable response with the function urlopen().
response = urlopen(request)

# Extract the response using the read() method and store the result in the variable: html.
html = response.read()

# Print the html
print(html)

# Close the response
response.close()