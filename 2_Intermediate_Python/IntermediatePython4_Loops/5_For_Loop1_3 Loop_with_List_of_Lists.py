# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Loop showing each room and it's area.
for room, area in house:
    print('The ' + str(room) + ' is ' + str(area) + 'sqm.')