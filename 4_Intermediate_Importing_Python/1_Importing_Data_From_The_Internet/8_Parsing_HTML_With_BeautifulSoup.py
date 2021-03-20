# Web Scraping
# Parsing HTML with BeautifulSoup


# Import Packages
# Import the function BeautifulSoup from the package bs4
import requests
from bs4 import BeautifulSoup

# Assign the URL to the variable: url
url = 'https://www.python.org/~guido/'

# Package the request to the URL, send the request and catch the response with a single
# function requests.get(), assigning the response to the variable: r.
r = requests.get(url) # In industry worded as "Package the request, send the request and catch the response: r"

# Use the text attribute of the object r to return the HTML of the webpage as a string;
# store the result in a variable: html_doc.
html_doc = r.text

# Create a BeautifulSoup object called, soup, from the resulting HTML using the function BeautifulSoup()
soup = BeautifulSoup(html_doc)

# Use the method prettify() on soup and assign the result to pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)
