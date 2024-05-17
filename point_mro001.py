class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    def __repr__(self):
        return f"({self.x};{self.y})"
    def dist(self,other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    def tr_area(p1,p2,p3):
        return 0.5*(p1.x*(p2.y - p3.y) + p2.x*(p3.y - p1.y) + p3.x*(p1.y - p2.y))
    def re_area(w,t,z):
        n = w.dist(t)
        m = t.dist(z)
        return n*m



