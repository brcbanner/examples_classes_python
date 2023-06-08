'''
Matrix class with attribute m representing the matrix 
as list of lists and with the following methods:

1) _getRows_ which returns the number of rows

2) _getCols_ which returns the number of columns

3) _getTrace_ which calculates and returns the trace (sum of diagonal 
   elements) if the matrix is square and prints 'error' otherwise

4) _getDet_ which calculates the determinant by Laplace’s theorem
                                                    
5) _getStats_ which calcluates the average value, the minimum value and 
   the maximum value
                                                    
6) _getTransposed_ which returns the transposed matrix
                                                    
7) _isSym_ which checks if it is symmetric                                                

8) _isMagic_ checks if it is a magic square and to be so it must:
    - be square
    - contain all distinct values
    - return the same sum in each row, each column and both diagonals

9) _isLatin_ checks if it is a latin square and to be so it must:
    - be square
    - contain values between 1 and n (where 'n' is the matrix size)
    - have on the same row/column all distinct values                                              
'''

class Matrix:
    
    def __init__(self, data):
        self.m = data
        
    def __repr__(self): 
        for r in self.m:
            print(r)
    
    ''' 1 '''
    def getRows(self):
        return len(self.m)
    
    ''' 2 '''
    def getCols(self):
        return len(self.m[0])
    
    ''' 3 '''
    def getTrace(self):
        if self.getRows() == self.getCols():
            s = 0
            for i in range(self.getRows()):
                s += self.m[i][i]
            return s
        else:
            return 'error'
    
    ''' 4 '''
    def getDet(self, n_row):
        
        if self.getRows() == self.getCols():
            n = self.getRows()
            
            if n == 1:
                return self.m[0][0]
           
            elif n == 2:
                return self.m[0][0]*self.m[1][1] - self.m[0][1]*self.m[1][0]
            
            else:
                list_new_m = [] # list containing all sub-matrices which
                                # do not contain 'n_row-1,j1' elements
                
                list_elements = [] # list containing 'n_row-1,j1' elements
                
                for j1 in range(n): # cycle on columns
                    
                    new_m = [] # sub_matrix which do not contain 'n_row-1,j1' elements
                    
                    for i in range(n): # cycle on rows
                        
                        r = [] # new row
                        
                        for j2 in range(n): # cycle on columns
                            
                            if j2 != j1 and i != n_row - 1: # conditions for taking items which
                                                            # are not of the 'n_row-1,j1' type
                                r.append(self.m[i][j2])
                        
                        if len(r) != 0: # in this way I don’t insert blank rows
                            new_m.append(r)
                    
                    new_M = Matrix(new_m)
                    list_new_m.append(new_M)
                    list_elements.append(self.m[n_row-1][j1])
                
                det_tot = 0 # I initialize the matrix determinant
                for col in range(len(list_new_m)):
                    if list_elements[col] != 0:
                        det_tot += ((-1)**((n_row-1)+col)) * list_elements[col] * list_new_m[col].getDet(n_row)
                return det_tot
                    
        else:
            return 'Error'
   
    ''' 5 '''
    def getStats(self):
        avg = 0
        m = self.m[0][0]
        M = self.m[0][0]
        for i in range(self.getRows()):
            for j in range(self.getCols()):
                if self.m[i][j] > M:
                    M = self.m[i][j]
                elif self.m[i][j] < m:
                    m = self.m[i][j]
                avg += self.m[i][j]
        avg /= (self.getRows() * self.getCols())
        return avg, m, M
    
    ''' 6 '''
    def getTransposed(self):
        m_t = []
        for i in range (self.getRows()):
            m_t.append([0]*self.getCols())
        for i in range (self.getRows()):
            for j in range (self.getCols()):
                m_t[j][i] = self.m[i][j]
        m_transposed = Matrix(m_t)
        return m_transposed
    
    ''' 7 '''
    def isSym(self):
        if self.getTransposed().m == self.m:
            return 'The matrix is symmetrical'
        else:
            return 'The matrix is not symmetrical'
        
    ''' 8 '''
    def isMagic(self):
        if self.getRows() != self.getCols():
            return 'The matrix cannot be a magic square because it is not a square matrix'
        else:
            n = self.getRows() 
            s = sum(self.m[0]) # I initialize the value s as the sum of the first row of m
             
            # rows and columns
            for i in range (n):
                l1 = [] # list for rows
                l2 = [] # list for columns
                for j in range (n):
                    l1.append(self.m[i][j])
                    l2.append(self.m[j][i])
                # I check the various conditions for rows and columns...
                if sum(l1) != s or sum(l2) != s:
                    return 'Matrix does not represent a magic square'
             
            # diagonals
            l1 = [] # main diagonal (\)
            l2 = [] # the other diagonal (/)
            for i in range (n):
                l1.append(self.m[i][i])  
                l2.append(self.m[i][n-i-1])
            # I check the various conditions for diagonals...
            if sum(l1) != s or sum(l2) != s:
                return 'Matrix does not represent a magic square'
             
            # matrix elements
            l = []
            for i in range (n):
                for j in range (n):
                    l.append(self.m[i][j])
            if len(l) != len(set(l)):
                return 'Matrix does not represent a magic square'
         
            return 'Matrix represents a magic square!!'
        
   
    ''' 9 '''
    def isLatin(self):
        if self.getRows() != self.getCols():
            return 'The matrix cannot be a latin square because it is not a square matrix'
        else:
            n = self.getRows() # matrix size
             
            for i in range (n):
                 
                # I check that on the line a value does not repeat
                if len(set(self.m[i])) != len (self.m[i]): 
                    return 'Matrix does not represent a latin square'
                 
                else:
                    for j in range (n):
                         
                        # I check that all values are between 1 and n
                        if self.m[i][j] < 1 or self.m[i][j] > n:
                            return 'Matrix does not represent a latin square'
             
            for j in range (n):
                l = []
                for i in range (n):
                    l.append(self.m[i][j])
                 
                # check on column...
                if len(l) != len(set(l)):
                    return 'Matrix does not represent a latin square'
             
            return 'Matrix represents a latin square!!'