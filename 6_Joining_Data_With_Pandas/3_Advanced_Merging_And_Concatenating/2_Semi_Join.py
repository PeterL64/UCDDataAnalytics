# Performing a Semi-Join

# Merge non_mus_tcks and top_invoices on tid using an inner join. Save the result as tracks_invoices.
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid', how='inner')


# Use .isin() to subset the rows of non_mus_tck where tid is in the tid column of tracks_invoices.
# Save the result as top_tracks.
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group top_tracks by gid and count the tid rows. Save the result to cnt_by_gid.
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge cnt_by_gid with the genres table on gid and print the result.
print(cnt_by_gid.merge(genres, on='gid'))