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


def mataddscalar(A, b):
    '''
    input: matrix A and scalar b
    output: result of element-wise addition of b on A
    '''
    n, m = len(A), len(A[0])
    added = []
    for i in range(n):
        row = []
        for j in range(m):
            row += [A[i][j]+b]
        added += [row]
    return added


def matadd(A, B):
    '''
    input: matrix A and B of same size n by m
    output: result of element-wise addition of A and B
    '''
    n, m = len(A), len(A[0])
    added = []
    for i in range(n):
        row = []
        for j in range(m):
            row += [A[i][j]+B[i][j]]
        added += [row]
    return added


def matsub(A, B):
    '''
    input: matrix A and B of same size n by m
    output: result of element-wise subtraction of A and B
    '''
    n, m = len(A), len(A[0])
    subtracted = []
    for i in range(n):
        row = []
        for j in range(m):
            row += [A[i][j]-B[i][j]]
        subtracted += [row]
    return subtracted


def matmulscalar(A, b):
    '''
    input: matrix A and scalar b
    output: result of element-wise multiplication of b on A
    '''
    n, m = len(A), len(A[0])
    added = []
    for i in range(n):
        row = []
        for j in range(m):
            row += [A[i][j]*b]
        added += [row]
    return added


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


def identity(n, m=None):
    '''
    input: size of a matrix (n by m)
    output: a corresponding identity matrix
    '''
    m = n if m is None else m
    E = [1] * min(n,m)
    return ele2diag(E,n,m)


def zero(n, m=None):
    '''
    input: size of a matrix (n by m)
    output: a corresponding zero matrix
    '''
    m = n if m is None else m
    E = [0] * min(n,m)
    return ele2diag(E,n,m)


def tri(A, direction=0):
    '''
    input: any matrix A and the desired direction of triangle(upper: 1, lower: 0)
    output: upper or lower trianglular matrix of A
    '''
    n, m = len(A), len(A[0])
    triangular = []
    for i in range(n):
        row = A[i][:]
        for j in range(m):
            if direction:
                if i>j:row[j]=0
            else:
                if i<j:row[j]=0
        triangular+=[row]
    return triangular


def triu(A):
    return tri(A,1)


def tril(A):
    return tri(A,0)


def toeplitz(P, T):
    '''
    input: list P and T to be combined to make a toeplitz matrix
    output: a corresponding toeplitz matrix A
    '''
    n, m = len(P), len(T)
    A = []
    for i in range(n):
        row = []
        for j in range(m):
            if i>j:row+=[P[i-j]]
            else:row+=[T[j-i]]
        A+=[row]
    return A


def bidiag(A, direction=0):
    '''
    input: any matrix A and the desired direction of additional diagonal(upper: 1, lower: 0)
    output: upper or lower bidiagonal matrix of A
    '''
    n, m = len(A), len(A[0])
    bidiagonal = []
    for i in range(n):
        row = A[i][:]
        for j in range(m):
            if direction:
                if i>j or i<j-1:row[j]=0
            else:
                if i<j or i>j+1:row[j]=0
        bidiagonal+=[row]
    return bidiagonal


def bidiagu(A):
    return bidiag(A,1)


def bidiagl(A):
    return bidiag(A,0)


def householder(V):
    '''
    input: vector V to make householder matrix H
    output: householder matrix H made from vector V
    '''
    n = len(V)
    outer = outer_product(V, V)
    inner = inner_product(V, V)
    H = matsub(identity(n), matmulscalar(outer, 2 / inner))
    return H


def outer_product(U, V):
    '''
    input: vector U and V
    output: result of outer product of vector U and V
    '''
    n = len(U)
    m = len(V)
    outer = []
    for i in range(n):
        row = []
        for j in range(m):
            row += [U[i]*V[j]]
        outer += [row]
    return outer


def inner_product(U, V):
    '''
    input: vector U and V
    output: result of inner product of vector U and V
    '''
    n = len(U)
    inner = 0
    for i in range(n):
        inner += U[i]*V[i]
    return inner


def solve_linear(A,B):
    '''
    input: matrix A and vector B
    output: solution X of A * X = B
    '''
    X, Y, n = deepcopy(A), deepcopy(B), len(A)
    for i in range(n):
        print(f'== operating row {i} ==')
        t = 1 / X[i][i] if X[i][i] else 0
        X[i], Y[i] = [e * t for e in X[i]], Y[i] * t
        display(X[i],0,1)
        display(Y[i])
        for j in range(n):
            if i==j:continue
            print(f'\t== operating row {j} ==')
            X_temp = [e * -X[j][i] for e in X[i]]
            Y_temp = Y[i] * -X[j][i]
            for k in range(len(X[i])):X[j][k] += X_temp[k]
            Y[j] += Y_temp
            display(X,1)
            display(Y,1)
            print(f'\t== row {j} is done ==')
        print(f'== row {i} is done ==')
    return ' '.join([f'{y:.3f}'for y in Y])


def deepcopy(A):
    '''
    input: any matrix A
    output: copy of matrix A
    '''
    if type(A[0])==list:
        n = len(A);copied = []
        for i in range(n):copied += [A[i][:]]
        return copied
    else:return A[:]


def display(A,indent=0,horizontal=0):
    '''
    print matrix or vector in a desired format
    input: any matrix or vector A
    output: none
    '''
    if type(A)==float or type(A)==int:
        print('\t'*indent,f'{A:.3f}')
    elif type(A[0])==list:
        for a in A:
            print('\t'*indent,end='')
            for e in a:print(f'{e:.3f}',end=' ')
            print()
    else:
        if horizontal:
            print('\t'*indent,end='')
            for a in A:print(f'{a:.3f}',end=' ')
            print()
        else:
            for a in A:print('\t'*indent,f'{a:.3f}')


def det_rec(A):
    '''
    input: a square matrix
    output: determinant of the matrix
    '''
    n = len(A)
    det = 0
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        for i in range(n):
            sign = (-1) ** i
            sub_det = det_rec([A[k][:i]+A[k][i+1:] for k in range(1,n)])
            det += sign * A[0][i] * sub_det
        return det


def det_tri(A):
    '''
    input: a squre matrix
    output: determinant of the matrix
    '''
    n = len(A)
    X = deepcopy(A)
    n_row_change = 0
    for i in range(n):
        if X[i][i] == 0:
            X[i], X[i+1] = X[i+1], X[i]
            n_row_change += 1
        for j in range(i+1,n):
            ratio = X[j][i] / X[i][i]            
            for k in range(n):X[j][k] -= ratio * X[i][k] # X[j] = matsub([X[j]], matmulscalar([X[i]], ratio))[0]
    det=1
    for i in range(n):det *= X[i][i]
    return (-1) ** n_row_change * det


def inv(A):
    '''
    input: a invertible matrix A
    output: inverted matrix of A
    '''
    n = len(A)
    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            minor = det_rec([[A[k][l] for l in range(n) if l!=j] for k in range(n) if k!=i])
            cofactor = (-1)**(i+j) * minor
            row += [cofactor]
        cofactors += [row]
    adjugate = transpose(cofactors)
    return matmulscalar(adjugate, 1/det_rec(A))