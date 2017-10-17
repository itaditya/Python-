"""
The following is an implementation that takes to python lists and returns the
dot product. If the lists are of different lengths or types, an error is printed.
"""
from functools import reduce

def dot_product(first_list, second_list):
    if(len(first_list) == len(second_list)):
        try:
            # multiply the two list items, and add them to the current total
            # We use zip to interlace the two lists into one, then we run lambda functions to multipy each value together and then add
            dot_product = reduce(lambda y1, y2: y1 + y2, map(lambda x: reduce(lambda x1, x2: x1*x2, x), zip(first_list, second_list)))
        except:
            print("One of your lists has an invalid type")
            return
        return dot_product
    else:
        print("The lists are not of the same length")
