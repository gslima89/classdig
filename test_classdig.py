
import unittest
import numpy as np

from classdig import fatmatriz


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
 
    def test_np_qr_decomp_1(self):
        n,p,m = 3,2,4
        W = np.array([[-0.73, 0.77],
            [-0.80, -0.29],
            [0.60, 0.01]])
        A = np.array([[-0.63, -0.30, 0.97, 0.72],
            [-0.40, -0.73, 0.94, -0.60],
            [-0.35, 0.75, -0.51, 0.51]])
        W_expected = np.array([[1.2381033882516, -0.2617713537297],
                        [0.0000000000000, 0.7801126574838],
                        [0.0000000000000, 0.0000000000000]])
        A_expected = np.array([[0.4603008160771, 1.0120317995167, -1.4264559945144, 0.2103216924135],
                        [-0.3231666988531, 0.3244671545177, 0.1227959607642, 1.0108234837328],
                        [-0.6025665469234, 0.2364586695515, 0.1863986258909, 0.2692594853198]])
        fatmatriz.np_qr_decomp(W,A,n,p,m)
        np.testing.assert_almost_equal(W_expected, W, 12)
        np.testing.assert_almost_equal(A_expected, A, 12)

    def test_sol_lin_system_1(self):
        n,p,m = 3,2,3
        A = np.array([[0.3, 0.6, 0.0],[0.5, 0.0, 1.0],[0.4, 0.8, 0.0]])
        W = np.array([[0.6,0],[0,1],[0.8,0]])
        H_expected = np.array([[0.5, 1.0, 0.0], [0.5, 0.0, 1.0]])
        H_obtained = fatmatriz.np_sol_lin_system(W,A,n,p,m)
        np.testing.assert_almost_equal(H_expected, H_obtained, 12)

    
# Roda testes para o modulo fatmatriz
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFatMatriz)
unittest.TextTestRunner(verbosity=2).run(suite1)