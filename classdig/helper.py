
from math import sqrt
from random import random


def print_matrix(W,n,m):
    for i in range(n):
        print('|', end='  ')
        for j in range(m):
            print('{0:+.4f}'.format(W[i][j]), end='  ')
        print('|')
    print('')


def zero_matrix(n,m):
    return [[0 for _ in range(m)] for _ in range(n)]

def random_matrix(n,m):
    return [[random() for _ in range(m)] for _ in range(n)]


def copy_matrix(A,n,m):
    return [[A[i][j] for j in range(m)] for i in range(n)]


def transpose_matrix(A,n,m):
    return [[A[j][i] for j in range(n)] for i in range(m)]


def non_neg_matrix(A,n,m):
    return [[max(0, A[i][j]) for j in range(m)] for i in range(n)]


def vector_norm(v,n):
    return sqrt(sum([v[i] ** 2 for i in range(n)]))


def normalize_matrix(A,n,m):
    col_norm = [vector_norm([A[i][j] for i in range(n)], n) for j in range(m)]
    return [[A[i][j]/col_norm[j] for j in range(m)] for i in range(n)]