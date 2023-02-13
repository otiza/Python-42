'''Column vectors as list of lists of single float ([[1.], [2.], [3.]]),
Row vectors  as a list of a list of several floats ([[1., 2., 3.]]).'''


class Vector:
    def __init__(self, *args):
        self.values = []
        if len(args) == 1 and isinstance(args[0], int) and args[0] > 0:
            self.shape = (args[0],1)
            for i in range(args[0]):
                self.values.append([float(i)])
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1],int) \
            and args[0] <= args[1]:
            self.shape = (args[1] - args[1],1)
            for i in range(args[1] - args[0]):
                self.values.append([float(i)])
        elif len(args) == 1 and isinstance(args[0], list):
            n = len(args[0])
            if n == 0:
                self.shape = (0,0)
            elif not isinstance(args[0][0],list):
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
        
    def __add__(self, other):
        if not isinstance(self,Vector) or self.shape != other.shape:
            raise ValueError("must be vectors of same shape")
        
