"""
1. Galilean Moons of Jupiter
Write a program that creates a dictionary containing the names of the Galilean moons of
Jupiter as keys and their mean radiuses (in kilometers) as values. The dictionary should
contain the following key-value pairs:
Moon Name (key) Mean Radius (value)
Io 1821.6
Europa 1560.8
Ganymede 2634.1
Callisto 2410.3
The program should also create a dictionary containing the moon names and their surface
gravities (in meters per second squared). The dictionary should contain the following key value pairs:
Moon Name (key) Surface Gravity (value)
Io 1.796
Europa 1.314
Ganymede 1.428
Callisto 1.235
The program should also create a dictionary containing the moon names and their orbital
periods (in days). The dictionary should contain the following key-value pairs:
Moon Name (key) Orbital Period (value)
Io 1.769
Europa 3.551
Ganymede 7.154
Callisto 16.689

The program should let the user enter the name of a Galilean moon of Jupiter, then it
should display the moon’s mean radius, surface gravity and orbital period.

@author Sharaf Qeshta
"""

MEAN_RADIUS = {
    "Io": 1821.6,
    "Europa": 1560.8,
    "Ganymede": 2634.1,
    "Callisto": 2410.3
}

SURFACE_GRAVITY = {
    "Io": 1.796,
    "Europa": 1.314,
    "Ganymede": 1.428,
    "Callisto": 1.235
}

ORBITAL_PERIOD = {
    "Io": 1.769,
    "Europa": 3.551,
    "Ganymede": 7.154,
    "Callisto": 16.689
}


def main():
    moon_name = input("enter the name of a Galilean moon of Jupiter: ")
    print(f"mean radius for {moon_name} is : {MEAN_RADIUS.get(moon_name, 'moon name not found')}")
    print(f"surface gravity for {moon_name} is : {SURFACE_GRAVITY.get(moon_name, 'moon name not found')}")
    print(f"orbital period for {moon_name} is : {ORBITAL_PERIOD.get(moon_name, 'moon name not found')}")


main()
