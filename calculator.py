# https://github.com/alugo3-star/lab10-JG-AL.git
# Partner 1: Joseph Gedaly
# Partner 2: Andres Lugo


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


import math

# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/ a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <=0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError

def hypotenuse(a, b):
    math.hypot(a, b)