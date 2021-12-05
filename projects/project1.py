# Computer Project #1
# Score 15/15
# program prompts for input, performs arithmetic on then displays the results.
# prompts for a floating point value
# perform conversion on floating point value
# displays result to nearest 3 decimal point


rods_distance = input('Please enter a floating point number: ')
rod = float(rods_distance)
meter = rod * 5.0292  # 1 rod = 5.0292 meters
feet = meter/0.3048  # 1 Foot = 0.3048 meters
mile = meter/1609.34  # 1 Mile = 1609.34 meters
furlong = rod/40  # 1 Furlong = 40 rods
minToWalk = (mile/3.1)*60  # 1 hour = 60 minutes, 3.1 miles per 60 minutes
print(rods_distance)

print("Input rods: ", rods_distance, "\n" "You input ", rod)
print("Conversions")
print("Meters: ", round(meter, 3), "\n" "Feet: ", round(feet, 3), "\n" "Miles: ", round(mile, 3),
      "\n" "Furlongs: ", round(furlong, 3), "\n" "Minutes to walk: ", round(minToWalk, 3))
