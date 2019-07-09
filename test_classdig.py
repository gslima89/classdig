
import unittest

from classdig import fatmatriz
from classdig import helper


class TestFatMatriz(unittest.TestCase):

    def test_c_s_1(self):
        c,s = fatmatriz._c_s(1,1)
        self.assertAlmostEqual(c,-0.707106781186547,15)
        self.assertAlmostEqual(s,0.707106781186547,15)
    
    def test_c_s_2(self):
        c,s = fatmatriz._c_s(-1,1)
        self.assertAlmostEqual(c,0.707106781186547,15)
        self.assertAlmostEqual(s,0.707106781186547,15)
    
    def test_c_s_3(self):
        c,s = fatmatriz._c_s(-3,5)
        self.assertAlmostEqual(c,0.514495755427527,15)
        self.assertAlmostEqual(s,0.857492925712544,15)

    def test_c_s_4(self):
        c,s = fatmatriz._c_s(2,-1)
        self.assertAlmostEqual(c,0.894427190999916,15)
        self.assertAlmostEqual(s,0.447213595499958,15)

    def test_c_s_5(self):
        c,s = fatmatriz._c_s(-2,-3)
        self.assertAlmostEqual(c,-0.554700196225229,15)
        self.assertAlmostEqual(s,0.832050294337844,15)

    def test_qr_decomp_1(self):
        n,p,m = 3,2,4
        W = [[-0.73, 0.77],
            [-0.80, -0.29],
            [0.60, 0.01]]
        A = [[-0.63, -0.30, 0.97, 0.72],
            [-0.40, -0.73, 0.94, -0.60],
            [-0.35, 0.75, -0.51, 0.51]]
        W_expected = [[1.2381033882516, -0.2617713537297],
                        [0.0000000000000, 0.7801126574838],
                        [0.0000000000000, 0.0000000000000]]
        A_expected = [[0.4603008160771, 1.0120317995167, -1.4264559945144, 0.2103216924135],
                        [-0.3231666988531, 0.3244671545177, 0.1227959607642, 1.0108234837328],
                        [-0.6025665469234, 0.2364586695515, 0.1863986258909, 0.2692594853198]]
        fatmatriz.qr_decomp(W,A,n,p,m)
        for i in range(n):
            for j in range(p):
                self.assertAlmostEqual(W_expected[i][j], W[i][j], 12)
            for j in range(m):
                self.assertAlmostEqual(A_expected[i][j], A[i][j], 12)

    def test_sol_lin_system_1(self):
        n,p,m = 3,2,3
        A = [[0.3, 0.6, 0.0],[0.5, 0.0, 1.0],[0.4, 0.8, 0.0]]
        W = [[0.6,0],[0,1],[0.8,0]]
        H_expected = [[0.5, 1.0, 0.0], [0.5, 0.0, 1.0]]
        H_obtained = fatmatriz.sol_lin_system(W,A,n,p,m)
        self.assertAlmostEqual(H_expected, H_obtained, 15)

    def test_nmf_1(self):
        #TODO: no minimo um teste mockando random_matrix
        pass


#TODO: Fazer testes para o modulo helper
class TestHelper(unittest.TestCase):

    def test_simple_norm_matrix_1(self):
        n,m = 3,3
        A = [[255, 255, 255],[255, 255, 255],[255, 255, 255]]
        H_expected = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]
        H_obtained = helper.simple_norm_matrix(A,n,m,255)
        for i in range(n):
            for j in range(m):
                self.assertAlmostEqual(H_expected[i][j], H_obtained[i][j], 15)

    def test_simple_norm_matrix_2(self):
        n,m = 4,2
        A = [[82, 99],[25, 24],[140, 0],[38, 178]]
        H_expected = [[0.5125, 0.61875],[0.15625, 0.15],[0.875, 0],[0.2375, 1.1125]]
        H_obtained = helper.simple_norm_matrix(A,n,m,160)
        for i in range(n):
            for j in range(m):
                self.assertAlmostEqual(H_expected[i][j], H_obtained[i][j], 15)

    def test_transpose_matrix(self):
        n,m = 4,3
        A = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
        H_expected = [[1,4,7,10],[2,5,8,11],[3,6,9,12]]
        H_obtained = helper.transpose_matrix(A,n,m)
        self.assertEqual(H_expected, H_obtained)
    
    def test_non_neg_matrix(self):
        n,m = 4,2
        eps =  1e-9
        A = [[-1,1],[-3,2],[-0.0001,4],[5,-1209]]
        H_expected = [[eps,1],[eps,2],[eps,4],[5,eps]]
        H_obtained = helper.non_neg_matrix(A,n,m)
        for i in range(n):
            for j in range(m):
                self.assertAlmostEqual(H_expected[i][j], H_obtained[i][j], 15)

    def test_vector_norm(self):
        v = [72.7989, 50.8903, 25.0375, 45.8051, 48.1874]
        norm_expected = 113.738786639915
        norm_obtained = helper.vector_norm(v,5)
        self.assertAlmostEqual(norm_expected, norm_obtained, 12)

    def test_column_norm(self):
        n,m = 3,4
        A = [[72.9997, 67.4640, 62.6658, 65.4024],
            [32.6425, 18.5230, 10.3482, 93.1086],
            [76.8785, 70.1975, 94.7211, 24.3043]]
        col_norm_expected = [110.926970429152, 99.106921207603, 114.044616348559, 116.350265655949]
        col_norm_obtained = helper.column_norm(A,n,m)
        for i in range(m):
            self.assertAlmostEqual(col_norm_expected[i], col_norm_obtained[i], 12)

    def test_normalize_matrix(self):
        n,m = 3,4
        A = [[72.9997, 67.4640, 62.6658, 65.4024],
            [32.6425, 18.5230, 10.3482, 93.1086],
            [76.8785, 70.1975, 94.7211, 24.3043]]
        H_expected = [[0.658087926836730, 0.680719360242063, 0.549484947263728, 0.562116464722105],
                    [0.2942701840112760, 0.186899156731942, 0.090738171878034, 0.800243982900086],
                    [0.6930550767101450, 0.708300683187956, 0.830561783911835, 0.208889080424349]]
        H_obtained = helper.normalize_matrix(A,n,m)
        for i in range(n):
            for j in range(m):
                self.assertAlmostEqual(H_expected[i][j], H_obtained[i][j], 12)

    def test_partial_prod_matrix(self):
        p,i,j = 2,1,1
        W = [[23.1216, 74.7233],
            [2.8524, 92.5912],
            [83.8608, 27.6582]]
        H = [[87.3661, 86.4335],
            [41.2079, 49.0017]]
        prod_expected = 4783.669120440
        prod_obtained = helper.partial_prod_matrix(W,H,p,i,j)
        self.assertAlmostEqual(prod_expected, prod_obtained, 12)

    def test_sq_error(self):
        n,p,m = 3,2,2
        W = [[23.1216, 74.7233],
            [2.8524, 92.5912],
            [83.8608, 27.6582]]
        H = [[87.3661, 86.4335],
            [41.2079, 49.0017]]
        A = [[5106.9603, 5663.1796],
            [4068.1774, 4787.5724],
            [8469.2303, 8605.5714]]
        error_expected = [8.95914884986818, 5.34840317762131]
        error_obtained = helper.sq_error(W, H, A, n, p, m)
        for i in range(m):
            self.assertAlmostEqual(error_expected[i], error_obtained[i], 12)

    
# Roda testes para o modulo fatmatriz
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFatMatriz)
unittest.TextTestRunner(verbosity=2).run(suite1)

# Roda testes para o modulo helper
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestHelper)
unittest.TextTestRunner(verbosity=2).run(suite2)
