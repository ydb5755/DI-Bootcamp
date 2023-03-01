import math
import copy
def get_rad_or_diam():
    while True:
        rad_or_diam = input("Please enter R for radius or D for diameter and we will compute the other: ")
        if rad_or_diam == "R" or rad_or_diam == "D":
            break
    return rad_or_diam

def get_value_of_rad_or_diam():
    while True:
        num_of_rad_or_diam = input("Please enter the value of what you chose above: ")
        try:
            int(num_of_rad_or_diam)
            break
        except:
            try:
                float(num_of_rad_or_diam)
                break
            except:
                print('please enter a number')
    return num_of_rad_or_diam

# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them

class Circle():
    def __init__(self, radiameter, value):
        # rad_or_diam = 'R' get_rad_or_diam()
        # value =  5 get_value_of_rad_or_diam()
        if radiameter == 'R':
            self.radius = value
            self.diameter = 2*self.radius
        elif radiameter == 'D':
            self.diameter = value
            self.radius = self.diameter/2
        elif radiameter == 'A': 
            self.radius = math.sqrt(value/math.pi)
            self.diameter = self.radius*2
        else:
            raise Exception('Invalid value for radiameter. Enter "R" or "D" or "A"')
        self.area = math.pi*math.pow(self.radius, 2)

    # def get_area(self):
    #     area = math.pi*math.pow(self.radius, 2)
    #     return area
     
    def __str__(self):
        return f'The radius of the circle is {self.radius} which gives it a diameter of {self.diameter} and an area of {self.get_area()} '

    def __add__(self, other):
        return Circle('A', self.area + other.area)
    
    def compare(self, other):
        if self.get_area() > other.get_area():
            return f'The larger circle has these dimensions: {self}'
        elif self.get_area() < other.get_area():
            return f'The larger circle has these dimensions: {other}'
        else:
            return 'The circles are equal in size'
        

def sort(*args):
    '''returns list of areas in ascending order'''
    lst = list(args)
    lst.sort(key=lambda x : x.area)
    return list(map(lambda x:x.area, lst))




round = Circle('R', 5)
rounder = Circle('D', 15)
roundest = round + rounder
print(sort(round, rounder, roundest))