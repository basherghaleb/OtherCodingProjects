# first program in python
# input two numbers, add them together, print them out
# wfp, 9/1/07; rje, 5/5/14

rods = input("Input rods: ")
rods_float = float(rods)
rods_str = str(rods_float)
rods_int = float(rods_str)

meters = (5.0292 * rods_int)
furlong = (rods_int / 40)
miles= (meters / 1609.34)
feet = (meters / 0.3048)
minstowalk = (miles*60/3.1)

meters_str = str(round(meters,3))
furlong_str = str(round(furlong,3))
miles_str = str(round(miles,3))
feet_str = str(round(feet,3))
minstowalk_str = str(round(minstowalk,3))

print("You input " + rods_str + " rods.")
print("\nConversions")
print("Meters: " + meters_str)
print("Feet: " + feet_str) 
print("Miles: " + miles_str)
print("Furlongs: " + furlong_str)
print("Minutes to walk " + rods_str + " rods: " + minstowalk_str)
