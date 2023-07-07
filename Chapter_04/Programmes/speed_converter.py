# This program converts the speeds 60 kph
# through 130 kph (in 10 kph increments)
# to mph.

START_SPEED = 60  # Starting speed
END_SPEED = 131  # Ending speed
INCREMENT = 10  # Speed increment
CONVERSION_FACTOR = 0.6214  # Conversion factor

# Print the table headings.
print('KPH\tMPH')
print('--------------')

# Print the speeds.
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(kph, '\t', format(mph, '.1f'))
