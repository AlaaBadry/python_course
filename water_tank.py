#!/usr/bin/python3

# This program is used to calculate volume and water flow of a Water Tank

# Input:

print("* Volume and Water flow program *")
side_length = int(input("Enter side length (m): "))
flow_speed = int(input("Enter flow speed (m/s): "))

# Processing

volume = side_length ** 3
time = volume * flow_speed

# Output:

print("Volume = ", volume, "m3")
print("Time = ", time, "s")
