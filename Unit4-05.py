# Created by: Gavin Zhou
# Created on: Nov 7 2017
# Created for: ICS3U

import math

print('Enter the radius')
input_radius = raw_input()
print('Enter the height')
input_height = raw_input()

def calculate_volume(radius,height):

    volume_of_cylinder = math.pi * (float(radius) ** 2) *float(height)

    return volume_of_cylinder
    
try:
    print('the volume of the cylinder is:' + str(round(calculate_volume(float(input_radius),
    float(input_height)), 2)))

except:
    print('input a number')








