
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


def rot_givens(w, n, m, i, j, c, s, k):
    """ Aplica rotacao de Givens na matriz W para as linha i e j
        utilizando a coluna k.
    """
    for r in range(k-1,m):
        aux = c * w[i][r] - s * w[j][r]
        w[j][r] = s * w[i][r] + c * w[j][r]
        w[i][r] = aux


def qr_decomp(w, b, n, m):
    """ Aplica decomposicao QR utilizando rotacoes de Givens """
    for k in range(m):
        for j in range(n-1,k,-1):
            if (w[j][k] != 0):
                i = j-1
                c,s = _c_s(w[i][k],w[j][k])
                rot_givens(w,n,m,i,j,c,s,k)
                rot_givens(b,n,1,i,j,c,s,k)


def sol_lin_system(w, b, n, m):
    """ Resolve o sistema linear """
    qr_decomp(w,b,n,m)
    x = [[0] for _ in range(m)]
    for k in range(m-1,-1,-1):
        x[k][0] += b[k][0]
        for j in range(k+1, m):
            x[k][0] -= w[k][j] * x[j][0]
        x[k][0] /= w[k][k]

    return x


if __name__ == "__main__":
    print('Testing...')
    n,m = 20,17
    #w = helper.random_matrix(n,m)
    #b = helper.random_matrix(n,1)
    #w = exemplos.w_exemplo_a(n,m)
    #b = exemplos.b_exemplo_a(n)
    w = exemplos.w_exemplo_b(n,m)
    b = exemplos.b_exemplo_b(n)
    #helper.print_matrix(w,n,m)
    #helper.print_matrix(b,n,1)
    x = sol_lin_system(w,b,n,m)
    helper.print_matrix(x,m,1)
    print('ok?')