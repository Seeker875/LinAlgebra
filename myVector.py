class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def minus(self,v):
        return(Vector([x-y for x,y in zip(self.coordinates,v.coordinates)]))  

    def plus(self,v):
        return(Vector([x+y for x,y in zip(self.coordinates,v.coordinates)]))  

    def scalarMult(self,c):
        return(Vector([c*x for x in self.coordinates]))       

    def magnitude(self):
        
        return(sum([x**2 for x in self.coordinates])**0.5)
        '''
        magnitude=0
        for x in self.coordinates:
            magnitude+=x**2
        return((magnitude)**0.5)
        '''
    def Normalize(self):
        try:
            return(self.scalarMult(1.0/self.magnitude()))  

        except ZeroDivisionError:
            raise Exception("Zero Vector can not be noramlized")

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
