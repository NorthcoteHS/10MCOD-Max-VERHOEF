"""
Prog:   rectCalc.py
Name:   Student Name
Date:   2018/04/18
Desc:   Calculates the area and perimeter of a circle.
"""

# Display welcome message
print('Welcome to the Circle Calculator!')

# Gets user to enter radius and converts to an intager
r = input('Enter a radius: ')
r = int(r)

# Find the area of the circle and displays
area = 3.14 * r * r
print('The area is', area)

# Finds the perimeter of the circle and displays
perimeter = 3.14 * r * 2
print('The perimeter is', perimeter)
