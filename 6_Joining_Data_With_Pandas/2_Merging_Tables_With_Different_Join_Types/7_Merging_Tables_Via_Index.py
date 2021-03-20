# Index merge for movie ratings

# Merge movies and ratings on the index and save to a variable called movies_ratings, ensuring that all of
# the rows from the movies table are returned.
movies_ratings = movies.merge(ratings, on='id', how='left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())


