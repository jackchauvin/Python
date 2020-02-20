import math

class Vector (object):
    """This class enables the creation of vectors in the form <x,y>"""
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def __str__(self):
        """Converts into a string"""
        return "<{:.2f},{:.2f}>".format(self.x,self.y)
    
    def __repr__(self):
        """ Convert vector into a string for use in the shell. """
        return "The vector is <{:.2f},{:.2f}>".format(self.x,self.y)
    
    def __add__(self,vector):
        """Adds two vectors"""
        new=Vector()
        new.x=self.x + vector.x
        new.y=self.x + vector.y
        return new
    
    def __sub__(self,vector):
        """subtracts two vectors"""
        new=Vector()
        new.x=self.x - vector.x
        new.y=self.x - vector.y
        return new
    
    def __mul__(self, scalar):
        """vector times a scalar"""
        vector=Vector()
        vector.x=self.x*scalar
        vector.y=self.y*scalar
        return vector
    
    def __rmul__(self, scalar):
        """Reverses multiplication if needed"""
        return self.__mul__(scalar)
        
    def __eq__(self, vector):
        """Checks for equality"""
        if self.x == vector.x and self.y == vector.y:
            return True
        else:
            return False
        
    def magnitude(self):
        """Finds the magnitude"""
        mag=math.sqrt(self.x**2 + self.y**2)
        return mag
    
    def unit(self):
        """Converts to a unit vector"""
        try:
            unit=Vector()
            unit.x=self.x/self.magnitude()
            unit.y=self.y/self.magnitude()
            return unit
        except ZeroDivisionError:
            return 'Cannot convert zero vector to a unit vector'