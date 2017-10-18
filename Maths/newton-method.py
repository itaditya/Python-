from math import *

def newton(guess, number):
    while(abs(guess*guess - number) > 0.001):
        guess = (guess + number/guess) / 2
    return guess

def my_sqrt(number):
    return newton(1, number)
