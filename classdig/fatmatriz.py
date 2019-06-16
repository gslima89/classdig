
from math import sqrt

from classdig import exemplos
from classdig import helper


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


def rot_givens(W, n, m, i, j, c, s, k):
    """ Aplica rotacao de Givens na matriz W para as linha i e j
        utilizando a coluna k.
    """
    for r in range(k-1,m):
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
                rot_givens(W,n,p,i,j,c,s,k)
                rot_givens(A,n,m,i,j,c,s,k)


def sol_lin_system(W, A, n, p, m):
    """ Resolve o sistema linear """
    qr_decomp(W,A,n,p,m)
    H = [[0 for _ in range(m)] for _ in range(p)]
    for k in range(p-1,-1,-1):
        for j in range(m):
            H[k][j] += A[k][j]
            for i in range(k+1, m):
                H[k][j] -= W[k][i] * H[i][j]
            H[k][j] /= W[k][k]

    return H


if __name__ == "__main__":
    print('Solving W x H = A')

    n,p,m = 20,17,3
    W = helper.random_matrix(n,p)
    A = helper.random_matrix(n,m)

    H = sol_lin_system(W,A,n,p,m)
    helper.print_matrix(H,p,m)

    print('ok?')