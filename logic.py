from math import pi
def circle(radius):
    radius = float(radius)
    if radius <= 0:
        raise TypeError
    else:
        return pi * (radius ** 2)
def square(side):
    side = float(side)
    if side <= 0:
        raise TypeError
    else:
        return side ** 2
def rectangle(length, width):
    length = float(length)
    width = float(width)
    if length <= 0 or width <= 0:
        raise TypeError
    else:
        return length * width
def triangle(base, height):
    base = float(base)
    height = float(height)
    if base <= 0 or height <= 0:
        raise TypeError
    else:
        return base * height * 0.5
