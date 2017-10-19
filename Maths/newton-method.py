from math import *

'''
Newton’s method to compute square roots x = a^(1/2)
for a > 0

to solve x^2 = a

The algorithm starts with some quess x_1 > 0 and computes
the sequence of impoved guesses

x_n+1 = (x_n + a/x_n)/2

see https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf for more detail
'''


# guess x until distance between x^2 and a is less than 0.001

def newton(x, a):  
    while(abs(x*x - a) > 0.001):
        x = (x + a/x) / 2
    return x

print(newton(1,36))
