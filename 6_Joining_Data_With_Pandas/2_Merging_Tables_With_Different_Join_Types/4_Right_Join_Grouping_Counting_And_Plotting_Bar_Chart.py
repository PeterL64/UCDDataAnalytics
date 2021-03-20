# Right Join with different column names

# two DataFrames can be merged by the movie ID but in df: pop_movies the column is called 'id', and in
# the df: movies_to_genres the column is called 'movie_id'.

# Merge movie_to_genres and pop_movies using a right join. Save the results as genres_movies.
genres_movies = movie_to_genres.merge(pop_movies, how='right', left_on='movie_id', right_on='id')

# Group genres_movies by genre and count the number of id values.
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()