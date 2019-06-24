
from math import sqrt
from sys import float_info

from classdig import exemplos
from classdig import helper

EPSILON = 10e-5

def _c_s(w_ik, w_jk):
    """  Calcula c e s para a rotacao de Givens  """
    if abs(w_ik) > abs(w_jk):
        t = - w_jk / w_ik
        c = 1/sqrt(1 + t ** 2)
        s = c * t
        return c, s
    else:
        t = - w_ik / w_jk
        s = 1/sqrt(1 + t ** 2)
        c = s * t
        return c, s


def rot_givens(W, n, m, i, j, c, s):
    """ Aplica rotacao de Givens na matriz W para as linha i e j
        utilizando a coluna k.
    """
    for r in range(m):
        aux = c * W[i][r] - s * W[j][r]
        W[j][r] = s * W[i][r] + c * W[j][r]
        W[i][r] = aux


def qr_decomp(W, A, n, p, m):
    """ Aplica decomposicao QR utilizando rotacoes de Givens """
    for k in range(p):
        for j in range(n-1,k,-1):
            if (W[j][k] != 0):
                i = j-1
                c,s = _c_s(W[i][k], W[j][k])
                rot_givens(W,n,p,i,j,c,s)
                rot_givens(A,n,m,i,j,c,s)


def sol_lin_system(W, A, n, p, m):
    """ Resolve o sistema linear """
    qr_decomp(W,A,n,p,m)
    H = helper.zero_matrix(p,m)
    for k in range(p-1,-1,-1):
        for j in range(m):
            H[k][j] += A[k][j]
            for i in range(k+1, p):
                H[k][j] -= W[k][i] * H[i][j]
            try:
                H[k][j] /= W[k][k]
            except ZeroDivisionError as err:
                #TODO: tratar melhor qndo tem divisao por zero
                print('Tratando: ', err)
                pass

    return H

def nmf(A, n, p, m, itmax = 100):
    """ Fatoracao por matrizes nao-negativas """
    W = helper.random_matrix(n,p)
    H = helper.zero_matrix(p,m)
    
    for _ in range(itmax):
        
        # copia da matriz A
        A2 = helper.copy_matrix(A,n,m)

        # normalizamos a matrix W
        W = helper.normalize_matrix(W,n,p)
        
        # solucao do sistema W x H = A
        H = sol_lin_system(W,A2,n,p,m)
        H = helper.non_neg_matrix(H,p,m)
        
        # solucao do sistema Ht x Wt = At
        At = helper.transpose_matrix(A,n,m)
        Ht = helper.transpose_matrix(H,p,m)
        Wt = sol_lin_system(Ht,At,m,p,n)
        
        # voltamos ao normal
        W = helper.transpose_matrix(Wt,p,n)
        W = helper.non_neg_matrix(W,n,p)

    return W