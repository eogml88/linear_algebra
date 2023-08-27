import functions.functions as f


A = [
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]
    ]

print(f'A: {A}')
print(f'transpose of A: \n{f.transpose(A)}')

print('matmul of A and transpose of A: ')
print(f.matmul(A,f.transpose(A)))

print('diagonlized A: ')
print(f.diag(A))

print('diagonal elements of A: ')
print(f.diag_ele(A))

print('diagonal matrix from diagonal elements of A: ')
print(f.ele2diag(f.diag_ele(A),3,4))

E = [1,10,1]

print(f'E: {E}')
print(f'a diagonal matrix D made from E: \n{f.ele2diag(E)}')

print('matmul of A and D: ')
print(f.matmul(A,f.ele2diag(E)))

print('matmul of D and A: ')
print(f.matmul(f.ele2diag(E),A))