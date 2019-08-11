
import numpy as np

from classdig import fatmatriz


def filename(fp, d):
    return fp + "train_dig{0}.txt".format(d)


def read_dig(fp, d, m, n=784):
    A = []
    for line in open(filename(fp, d)):
        line_list = line.split()
        A.append(line_list[0:m])
    return fatmatriz.simple_norm_matrix(A,n,m,weight=255)


def train_dig(fp, d, m, p, itmax = 100, n = 784):
    A = read_dig(fp,d,m,n)
    return fatmatriz.nmf(A, n, p, m, itmax)


def read_test(fp, m, n = 784):
    A = []
    for line in open(fp + "test_images.txt"):
        line_list = line.split()
        A.append(line_list[0:m])
    return fatmatriz.simple_norm_matrix(A,n,m,weight=255)


def read_index(fp):
    A = []
    for line in open(fp + "test_index.txt"):
        A.append(int(line))
    return np.array(A)


def test_images(W, A, n, p, m):
    A2 = A.copy()
    W2 = W.copy()
    H = fatmatriz.sol_lin_system(W2,A2,n,p,m)
    return fatmatriz.sq_error(W,H,A)


def statistics(fp, digs, n):
    index = read_index(fp)
    summary = [{"total": 0, "acertos": 0} for _ in range(10)]
    for i in range(n):
        summary[index[i]]["total"] += 1
        if index[i] == digs[i]:
            summary[index[i]]["acertos"] += 1
    return summary