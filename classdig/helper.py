
from random import random

def print_matrix(w,n,m):
    for i in range(n):
        print('|', end=' ')
        for j in range(m):
            print('{0:.4f}'.format(w[i][j]), end=' ')
        print('|')
    print('')


def random_matrix(n,m):
    return [[10*random() for _ in range(m)] for _ in range(n)]
