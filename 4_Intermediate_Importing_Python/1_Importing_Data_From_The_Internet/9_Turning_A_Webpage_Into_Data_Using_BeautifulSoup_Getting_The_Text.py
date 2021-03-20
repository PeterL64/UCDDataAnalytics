# Turning a webpage into data using BeautifulSoup: getting the text


# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get/Extract the title of Guido's webpage using the "title" attribute and assign to variable: guido_title
guido_title = soup.title

# Print the title of Guido's webpage
print(guido_title)

# Get Guido's text using the method get_text() and assign to the variable: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)