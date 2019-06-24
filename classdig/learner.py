
from classdig import helper
from classdig import fatmatriz


def filename(fp, d):
    return fp + "train_dig{0}.txt".format(d)


def read_dig(fp, d, m, n = 784):
    A = []
    for line in open(filename(fp, d)):
        line_list = line.split()
        A.append(line_list[0:m])
    return helper.simple_norm_matrix(A,n,m,weight=255)


def train_dig(fp, d, m, p, itmax = 100, n = 784):
    A = read_dig(fp, d, m)
    return fatmatriz.nmf(A,n,p,m,itmax)