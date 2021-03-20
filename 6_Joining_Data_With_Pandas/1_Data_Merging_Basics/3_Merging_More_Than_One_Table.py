# Merging/Joining Three Tables/DataFrames


# cal           ridership           stations
# year          station_id          station_id
# month         year                station_name
# day           month               location
# day_type      day
#               rides

# Merge the ridership and cal tables together, starting with the ridership table on the left
# and save the result to the variable ridership_cal.
ridership_cal = ridership.merge(cal, on=['year', 'month', 'day'])

# Extend the previous merge to three tables by also merging the stations table.
ridership_cal_stations = ridership.merge(cal, on=['year', 'month', 'day']) \
    .merge(stations, on='station_id')

# Use this criteria to find the filtering criteria; station_name == 'Wilson', day_type =='Weekday',
# month == 7
filter_criteria = ((ridership_cal_stations['month'] == 7)
                   & (ridership_cal_stations['day_type'] == 'Weekday')
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())
