
from math import sqrt
from sys import float_info
import numpy as np


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


def rot_givens(W, i, j, c, s):
    W[i,:], W[j,:] = c * W[i,:] - s * W[j,:], s * W[i,:] + c * W[j,:]


def qr_decomp(W, A, n, p, m):
    """ Aplica decomposicao QR utilizando rotacoes de Givens """
    for k in range(p):
        for j in range(n-1,k,-1):
            if (W[j,k] != 0):
                i = j-1
                c,s = _c_s(W[i,k], W[j,k])
                rot_givens(W,i,j,c,s)
                rot_givens(A,i,j,c,s)


def sol_lin_system(W, A, n, p, m):
    """ Resolve o sistema linear """
    qr_decomp(W,A,n,p,m)
    H = np.zeros((p,m))
    for k in range(p-1,-1,-1):
        for j in range(m):
            H[k,j] += A[k,j]
            for i in range(k+1, p):
                H[k,j] -= W[k,i] * H[i,j]
            H[k,j] /= W[k,k]

    return H


def normalize_matrix(W):
    return W / np.sqrt(np.sum(W ** 2, axis=0))


def simple_norm_matrix(A, n, m, weight = 1):
    return np.array([[int(A[i][j])/weight for j in range(m)] for i in range(n)])


def non_neg_matrix(W,n,m,epsilon = 1e-9):
    return np.array([[max(epsilon, W[i,j]) for j in range(m)] for i in range(n)])


def sq_error(W, H, A):
    E = W.dot(H) - A
    return np.sqrt(np.sum(E ** 2, axis=0))


def error(W, H, A):
    E = A - W.dot(H)
    return np.sqrt(np.sum(E ** 2))


def nmf(A, n, p, m, itmax = 100):
    """ Fatoracao por matrizes nao-negativas """
    W = np.random.rand(n,p)
    
    erro_ant = float_info.max
    epsilon = 1e-5

    for _ in range(itmax):
        
        # normalizamos a matrix W
        W = normalize_matrix(W)
        
        # solucao do sistema W x H = A
        H = sol_lin_system(W, A.copy(), n, p, m)
        H = non_neg_matrix(H, p, m)

        # solucao do sistema Ht x Wt = At
        Wt = sol_lin_system(np.transpose(H.copy()), np.transpose(A.copy()), m, p, n)

        # voltamos ao normal
        W = np.transpose(Wt)
        W = non_neg_matrix(W, n, p)

        erro_pos = error(W, H, A)
        if (abs(erro_ant - erro_pos) < epsilon):
            break
        erro_ant = erro_pos

    return W