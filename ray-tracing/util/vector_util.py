import math

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def magnitude(a):
    return math.sqrt(a[0]*a[0]+a[1]*a[1]+a[2]*a[2])

def minus(a, b):
    return [a[0] - b[0],a[1] - b[1],a[2] - b[2]]

def addition(a, b):
    return [a[0] + b[0],a[1] + b[1],a[2] + b[2]]

def multiplication(a, scalar):
    return [a[0] * scalar,a[1] * scalar,a[2] * scalar]

def division(a, scalar):
    return [a[0] / scalar,a[1] / scalar,a[2] / scalar]

def unit_vector(a):
    return division(a, magnitude(a))