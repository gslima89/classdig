from math import sqrt

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

def rot_givens(w, i, j, k):
    """ Aplica rotacao de Givens na matriz W para as linha i e j
        utilizando a coluna k.
    """

    m = len(w[0])
    c,s = _c_s(w[i][k],w[j][k])

    for r in range(m):
        aux = c * w[i][r] - s * w[j][r]
        w[j][r] = s * w[i][r] + c * w[j][r]
        w[i][r] = aux

if __name__ == "__main__":
    print('Testing...')
    w = [[1,2,3],[4,5,6],[7,8,9]]
    print(w)
    rot_givens(w,0,1,0)
    print(w)
    rot_givens(w,0,2,0)
    print(w)
    rot_givens(w,1,2,1)
    print(w)