from math import gcd
class fract:
    def __init__(self, n,d):
        if (d == 0):
            raise ZeroDivisionError
        t = gcd(n,d)
        self.n = n//t
        self.d = d//t
    def __sub__(self, other):
        return fract(self.n * other.d - other.n*self.d, self.d * other.d)
    def __add__(self, other):
        return fract(self.n * other.d + other.n*self.d, self.d * other.d)
    def __mul__(self, other):
        return fract(self.n * other.n, self.d * other.d)
    def __truediv__(self, other):
        return fract(self.n * other.d, self.d * other.n)
    def __pow__(self, other):
        return fract((self.n)**other, (self.d)**other)
    def __repr__(self):
        if self.n == self.d:
            return f"{self.n}"
        return f"{self.n}/{self.d}"
    def __abs__(self):
        return fract(abs(self.n), abs(self.d))
    
a = fract(-1,4)
b = fract(5,4)
c = 4

print(f"{a} - {b} = {a-b}")
print(f"{a} + {b} = {a+b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} ** {c} = {a**c}")
print(f"│{a}│ =  {abs(a)}")

