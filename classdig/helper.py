
from math import sqrt
from random import random
from sys import float_info


def print_matrix(W,n,m):
    for i in range(n):
        print('|', end='  ')
        for j in range(m):
            print('{0:+.4f}'.format(W[i][j]), end='  ')
        print('|')
    print('')


def simple_norm_matrix(A,n,m, weight = 1):
    return [[int(A[i][j])/weight for j in range(m)] for i in range(n)]


def zero_matrix(n,m):
    return [[0 for _ in range(m)] for _ in range(n)]


def one_matrix(n,m):
    return [[1 for _ in range(m)] for _ in range(n)]


def zero_vector(n):
    return [0 for _ in range(n)]


def one_vector(n):
    return [1 for _ in range(n)]


def max_vector(n):
    return [float_info.max for _ in range(n)]


def random_matrix(n,m):
    return [[random() for _ in range(m)] for _ in range(n)]


def copy_matrix(A,n,m):
    return [[A[i][j] for j in range(m)] for i in range(n)]


def transpose_matrix(A,n,m):
    return [[A[j][i] for j in range(n)] for i in range(m)]


def non_neg_matrix(A,n,m,epsilon = 1e-9):
    return [[max(epsilon, A[i][j]) for j in range(m)] for i in range(n)]


def vector_norm(v,n):
    return sqrt(sum([v[i] ** 2 for i in range(n)]))


def column_norm(A,n,m):
    return [vector_norm([A[i][j] for i in range(n)], n) for j in range(m)]


def normalize_matrix(A,n,m):
    col_norm = column_norm(A,n,m)
    return [[A[i][j]/col_norm[j] for j in range(m)] for i in range(n)]


def partial_prod_matrix(W,H,p,i,j):
    return sum([W[i][k] * H[k][j] for k in range(p)])


def sq_error(W,H,A,n,p,m):
    T = [[(partial_prod_matrix(W,H,p,i,j) - A[i][j]) for j in range(m)] for i in range(n)]
    return column_norm(T,n,m)