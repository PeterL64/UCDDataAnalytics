# Using the Append Method to Merge/Join Tables/DataFrames vertically rather than
# using the Concatenate Method.

# Use the .append() method to combine (in this order)tracks_ride, tracks_master,
# and tracks_st together vertically, and save to metallica_tracks.
metallica_tracks = tracks_ride.append([tracks_master,tracks_st], sort=False)

# Merge metallica_tracks and invoice_items on tid with an inner join, and save to tracks_invoices.
tracks_invoices = metallica_tracks.merge(invoice_items, on='tid', how='inner')

# For each tid and name in tracks_invoices, sum the quantity sold column, and save as tracks_sold.
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity':'sum'})

# Sort tracks_sold in descending order by the quantity column, and print the table.
print(tracks_sold.sort_values('quantity', ascending=False))