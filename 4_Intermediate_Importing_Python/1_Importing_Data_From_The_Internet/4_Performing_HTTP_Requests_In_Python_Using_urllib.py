# Performing HTTP GET requests using the urllib library packages urlopen and Request


# Import the functions urlopen and Request from the subpackage urllib.request
# Import Packages
from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# Package the request to the url, which is stored in the variable url,  using the function Request() and
# assign it to the variable: request
# This packages the request: request
request = Request(url)

# Send the request and catch the response in the variable: response using the function urlopen()
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Close the response
response.close()
