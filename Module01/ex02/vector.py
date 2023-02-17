'''Column vectors as list of lists of single float ([[1.], [2.], [3.]]),
Row vectors  as a list of a list of several floats ([[1., 2., 3.]]).'''


class Vector:
    def __init__(self, *args):
        self.values = []
        if len(args) == 1 and isinstance(args[0], int) and args[0] > 0:
            
            self.shape = (args[0],1)
            for i in range(args[0]):
                self.values.append([float(i)])
        elif len(args[0]) == 2 and isinstance(args[0][0], int) and isinstance(args[0][1],int) \
            and args[0][0] <= args[0][1]:
            
            self.shape = (args[0][1] - args[0][0],1)
            i = args[0][0]
            while i < args[0][1]:
                self.values.append([float(i)])
                i += 1
        elif len(args) == 1 and isinstance(args[0], list):
            
            n = len(args[0])
            if n == 0:
                self.shape = (0,0)
            elif  isinstance(args[0][0],list):
                
                self.shape = (n,1)
            else:
                self.shape = (1,n)
            for i in args[0]:
                if isinstance(i, float) or (isinstance(i,list) and isinstance(i[0],float)):
                    self.values = args[0]
                else:
                    raise ValueError("args should be floats")
                self.values = args[0]
        else:
            raise ValueError("invalid args")
        
    
    def __add__(self,other):
        if not isinstance(other, Vector):
            raise ValueError("must be vector")
        if not self.shape == other.shape:
            raise ValueError("Vectors must be of same shape")
        ret = Vector(self.values)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret.values[i][j] = self.values[i][j] + other.values[i][j]
        return ret 
    
    def __radd__(self,other):
        return self.__add__(other)
    
    def __sub__(self,other):
        if not isinstance(other, Vector):
            raise ValueError("must be vector")
        if not self.shape == other.shape:
            raise ValueError("Vectors must be of same shape")
        ret = Vector(self.values)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret.values[i][j] = self.values[i][j] - other.values[i][j]
        return ret 
    
    def __rsub__(self,other):
        return self.__sub__(other)
    
    def  __truediv__(self,other):
        if not isinstance(other, (int,float)):
            raise ValueError("must be scalar")
        ret = Vector(self.values)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret.values[i][j] = self.values[i][j] / other
        return ret 

    def __rtruediv__(self,other):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __mul__(self, other):
        if not isinstance(other, (int,float)):
            raise ValueError("must be scalar")
        ret = []
        print("----->",self.values[0])
        if self.shape[0] == 1:
            for i in self.values:
                ret.append(i * other)
        else:
            for i in self.values:
                for x in i:
                    ret.append([x * other])
        return ret

    def __rmul__(self,other):
        return self.__mul__(other)
    
    def __str__(self):
        return("Vector({})".format(self.values))
    
    def __repr__(self):
        print("Vector({})".format(self.values))

    def dot(self,other):
        if not isinstance(other, Vector):
            raise TypeError("Must be vector")
        if not self.shape == other.shape:
            raise ValueError("Vectors must be of same shape")
        ret = 0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret += self.values[i][j] * other.values[i][j]
        return ret

    

