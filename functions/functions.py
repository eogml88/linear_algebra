def transpose(A):
    '''
    input: any matrix A
    output: transpose of A
    '''
    n, m = len(A), len(A[0])
    A_transposed = []
    for j in range(m):
        row = []
        for i in range(n):
            row += [A[i][j]]
        A_transposed += [row]
    return A_transposed


def matmul(A, B):
    '''
    input: matrix A of size n by m and matrix B of size m by l
    output: result of matrix multiplication of A and B
    '''
    n, m, l = len(A), len(A[0]), len(B[0])
    multiplicated = []
    for i in range(n):
        row = []
        for j in range(l):
            sum_ = 0
            for k in range(m):
                sum_ += A[i][k] * B[k][j]
            row += [sum_]
        multiplicated += [row]
    return multiplicated


def diag(A):
    '''
    input: any matrix A
    output: diagonalized A
    '''
    n, m = len(A), len(A[0])
    A_diagonalized = []
    for i in range(n):
        row = []
        for j in range(m):
            if i==j:row += [A[i][j]]
            else:row += [0]
        A_diagonalized += [row]
    return A_diagonalized


def diag_ele(A):
    '''
    input: any matrix A
    output: array of diagonal elements of A
    '''
    n, m = len(A), len(A[0])
    diagonal_elements = []
    for i in range(min(n,m)):
        diagonal_elements += [A[i][i]]
    return diagonal_elements


def ele2diag(E, n=None, m=None):
    '''
    input: diagonal elements of a matrix
    output: a corresponding diagonal matrix
    '''
    n = len(E) if n is None else n
    m = n if m is None else m
    diagonal_matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            if i==j:row += [E[i]]
            else:row += [0]
        diagonal_matrix += [row]
    return diagonal_matrix


def identity(n,m=None):
    '''
    input: size of a matrix (n by m)
    output: a corresponding identity matrix
    '''
    m = n if m is None else m
    E = [1] * min(n,m)
    return ele2diag(E,n,m)


def zero(n,m=None):
    '''
    input: size of a matrix (n by m)
    output: a corresponding zero matrix
    '''
    m = n if m is None else m
    E = [0] * min(n,m)
    return ele2diag(E,n,m)


def tri(A,dir=0):
    '''
    input: any matrix A and the desired direction of triangle(upper: 1, lower: 0)
    output: upper or lower trianglular matrix of A
    '''
    n, m = len(A), len(A[0])
    triangular = []
    for i in range(n):
        row = A[i][:]
        for j in range(m):
            if dir:
                if i>j:row[j]=0
            else:
                if i<j:row[j]=0
        triangular+=[row]
    return triangular


def triu(A):
    return tri(A,1)


def tril(A):
    return tri(A,0)


def toeplitz(A, B):
    '''
    input: list A and B to be combined to make a toeplitz matrix
    output: a corresponding toeplitz matrix
    '''
    n, m = len(A), len(B)
    toeplitz = []
    for i in range(n):
        row = []
        for j in range(m):
            if i>j:row+=[A[i-j]]
            else:row+=[B[j-i]]
        toeplitz+=[row]
    return toeplitz