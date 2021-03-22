# Performing HTTP requests in Python using requests

# Import requests package
import requests

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r. (This is how is
# could be worded in a job).
# Package the request to the URL, send the request and catch the response with a
# single function requests.get(), assigning the response to the variable: r.
r = requests.get(url)

# Use the text attribute of the object r to return the HTML of the webpage as a string; store
# the result in a variable: text.
text = r.text

# Print the html
print(text)