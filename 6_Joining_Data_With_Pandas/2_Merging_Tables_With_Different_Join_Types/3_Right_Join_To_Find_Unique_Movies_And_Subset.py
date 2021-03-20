# Right Join to find Unique Movies

# Most scifi movies are considered action movies as well. Find the movies that are scifi only.

# Merge action_movies and scifi_movies tables with a right join on movie_id.
# Save the result as action_scifi
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right')

# Update the merge to add suffixes, where '_act' and '_sci' are suffixes for
# the left and right tables,respectively.
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right', suffixes=('_act', '_sci'))

# Print the first few rows of action_scifi to see the structure
print(action_scifi.head())

# From action_scifi, subset only the rows where the genre_act column is null.
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge movies and scifi_only using the id column in the left table and the movie_id column
# in the right table with an inner join.
movies_and_scifi_only = movies.merge(scifi_only, left_on='id', right_on='movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)