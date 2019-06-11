
def w_exemplo_a(n,m):
    w = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i == j):
                w[i][j] = 2
            elif (abs(i-j) == 1):
                w[i][j] = 1
    return w


def b_exemplo_a(n):
    return [[1] for _ in range(n)]


def w_exemplo_b(n,m):
    w = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (abs(i-j) <= 4):
                w[i][j] = 1/(i+j+1)
    return w


def b_exemplo_b(n):
    return [[i+1] for i in range(n)]
