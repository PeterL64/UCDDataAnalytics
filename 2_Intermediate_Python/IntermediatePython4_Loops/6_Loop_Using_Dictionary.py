# Creating a loop using a dictionary


# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for country, capital, in europe.items():
    print('The capital of ' + country + ' is ' + capital + '.')
