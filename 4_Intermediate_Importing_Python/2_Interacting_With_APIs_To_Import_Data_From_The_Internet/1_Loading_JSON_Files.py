# Loading JSON Files

# Load the JSON 'a_movie.json' into the variable: json_data, within the context provided by the "with" statement.
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Use a for loop to print all key-value pairs in the dictionary json_data. You can access a value
# in a dictionary using the syntax: dictionary[key]
for k in json_data.keys():
    print(k + ': ', json_data[k])
