"""
3. Lap Times
Write a program that asks the user to enter the number of times that they have run around
a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps.
When the loop finishes, the program should display the time of their fastest lap, the time of
their slowest lap, and their average lap time.

@author Sharaf Keshta
"""

laps = int(input("enter the number of times that you have run around the racetrack:"))

fastest_lap = 0
slowest_lap = 0
sum_of_laps_time = 0

for i in range(laps):
    lap_time = int(input(f"enter the time for the {i+1}th lap: "))
    if i == 0:
        slowest_lap = lap_time
    if lap_time < slowest_lap:
        slowest_lap = lap_time
    if lap_time > fastest_lap:
        fastest_lap = lap_time
    sum_of_laps_time += lap_time

print("your fastest lap is completed in ", fastest_lap, " minutes")
print("your slowest lap is completed in ", slowest_lap, " minutes")
print("your average to complete a single lap is ", format(sum_of_laps_time/laps, ".2f"), " minutes")