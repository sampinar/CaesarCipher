#!/usr/bin/env python3

# Exercise coordinate from week5 edx MITx: 6.00.1x
# Your task is to define the following two methods for the Coordinate class:

#  1. Add an __eq__ method that returns True if coordinates refer to same point in the plane (i.e., have the same x and y coordinate).

#  2. Define __repr__, a special method that returns a string that looks like a valid Python expression that could be used to recreate an object with the same value. In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.
# More on __repr__: https://stackoverflow.com/questions/452300/python-object-repr-self-should-be-an-expression

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    #def __str__(self):
    #    return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __repr__(self):
        return 'repr(' + str(self.x) + ')' + ' == ' + 'repr(' + str(self.y) + ')'

sup = Coordinate(4, 4)
print(sup.x)
print(sup.y)

print(sup.x == sup.y)

print(sup)