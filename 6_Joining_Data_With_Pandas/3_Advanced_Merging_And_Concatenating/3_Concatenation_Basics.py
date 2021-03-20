# Concatenation Basics

# Concatenate tracks_master, tracks_ride, and tracks_st, in that order, setting sort to True.
tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],sort=True)
print(tracks_from_albums)

# Concatenate tracks_master, tracks_ride, and tracks_st, where the index goes from 0 to n-1.
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],ignore_index=True ,sort=True)
print(tracks_from_albums)

# Concatenate tracks_master, tracks_ride, and tracks_st, showing only columns that are in all tables.
tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st], sort=True, join='inner')
print(tracks_from_albums)