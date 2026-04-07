import copy
classs Mat:
    def __init__(self,A):
        self.nr = len(A)
        self.nc=len(A[0])
        self.data = copy.deepcopy(A)
        
    def mul(self,b):
        
