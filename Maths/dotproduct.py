"""
The following is an implementation that takes to python lists and returns the
dot product. If the lists are of different lengths or types, an error is printed.
"""

def dot_product(first_list, second_list):
    dot_product = 0
    if(len(first_list) == len(second_list)):
        for i in range(0, len(first_list)):
            try:
                # multiply the two list items, and add them to the current total
                dot_product += (first_list[i] * second_list[i])
            except:
                print("One of your lists has an invalid type")
                return
        print(dot_product)
    else:
        print("The lists are not of the same length")
