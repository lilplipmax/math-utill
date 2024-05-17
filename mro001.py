from math import *
def f(x):
    try:
        if x < 1:
            return float((log(e*pi + abs(x/5))))

        elif 1<= x < 4:
            return float(abs(floor(x/5 - 3)))

        else:
            return float((atan(x/4) + 1/(2*x-9)))
    except:
        return None


def g(x,y):
    if ((x + 5)**2 + (y - 4)**2 < 100) and ((x + 5)**2 + (y - 4)**2 > 16) and (-1<x<7) and (-4< y < 5):
        return True
    else:
        return False


def h(a,b,c):
    if c == 0:
        if (a==3 or a == -3):
            return 'continuum'
        elif a != 3 and a!= -3:
            return '1'
    if  c != 0:
        if (b*c == 18 + 6*a) or (b*c == -18 + 6*a):
            return '2'
        elif (b*c != 18 + 6*a) and (b*c != -18 + 6*a):
            return '3'


