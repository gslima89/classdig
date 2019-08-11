
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
    
    def test_normalize_matrix(self):
        W = np.array([[1.8920, 3.1650, 9.8590],
                    [0.2370, 5.6520, 3.4650],
                    [0.7530, 8.7080, 5.5970],
                    [9.1210, 8.7450, 8.2790]])
        W_expected = np.array([[0.2023842159448, 0.2270777720624, 0.6818400114867],
                            [0.0253515111939, 0.4055113957968, 0.2396364377524],
                            [0.0805472064516, 0.6247687959304, 0.3870837350939],
                            [0.9756587915605, 0.6274234175943, 0.5725685622374]])
        W_obtained = fatmatriz.normalize_matrix(W)
        np.testing.assert_almost_equal(W_expected, W_obtained, 12)

    def test_simple_norm_matrix(self):
        n,m = 4,3
        A = [['106', '168', '129'],
            ['149', '13', '253'],
            ['23', '201', '70'],
            ['120', '240', '18']]
        A_expected = np.array([[0.4156862745098, 0.6588235294117, 0.5058823529411],
                    [0.5843137254901, 0.0509803921568, 0.9921568627450],
                    [0.0901960784313, 0.7882352941176, 0.2745098039215],
                    [0.4705882352941, 0.9411764705882, 0.0705882352941]])
        A_obtained = fatmatriz.simple_norm_matrix(A,n,m,weight=255)
        np.testing.assert_almost_equal(A_expected, A_obtained, 12)

    def test_non_neg_matrix(self):
        #non_neg_matrix(W,n,m,epsilon = 1e-14)
        n,m = 4,3
        epsilon = 1e-7
        W = np.array([[-0.0390, -0.4374, 0.9325],
                    [-0.3587, 0.2590, -0.8769],
                    [0.9965, -0.6924, 0.9869],
                    [-0.8498, -0.7005, -0.6305]])
        W_expected = np.array([[epsilon, epsilon, 0.9325],
                    [epsilon, 0.2590, epsilon],
                    [0.9965, epsilon, 0.9869],
                    [epsilon, epsilon, epsilon]])
        W_obtained = fatmatriz.non_neg_matrix(W, n, m, epsilon)
        np.testing.assert_almost_equal(W_expected, W_obtained, 12)


    def test_sq_error(self):
        W = np.array([[0.6164, 0.1555],
                    [0.9949, 0.1432],
                    [0.0625, 0.7198],
                    [0.9136, 0.9948]])
        H = np.array([[0.9892, 0.8141, 0.5983],
                    [0.6632, 0.6192, 0.8780]])
        A = np.array([[0.8421, 0.3401, 0.6322],
                    [0.5402, 0.0921, 0.5909],
                    [0.7095, 0.1460, 0.0431],
                    [0.8924, 0.1919, 0.3475]])
        erro_expected = np.array([0.8868474944829, 1.4845184306010, 1.2552241732008])
        erro_obtained = fatmatriz.sq_error(W,H,A)
        np.testing.assert_almost_equal(erro_expected, erro_obtained, 12)

    def test_qr_decomp_1(self):
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
        fatmatriz.qr_decomp(W,A,n,p,m)
        np.testing.assert_almost_equal(W_expected, W, 12)
        np.testing.assert_almost_equal(A_expected, A, 12)

    def test_sol_lin_system_1(self):
        n,p,m = 3,2,3
        A = np.array([[0.3, 0.6, 0.0],[0.5, 0.0, 1.0],[0.4, 0.8, 0.0]])
        W = np.array([[0.6,0],[0,1],[0.8,0]])
        H_expected = np.array([[0.5, 1.0, 0.0], [0.5, 0.0, 1.0]])
        H_obtained = fatmatriz.sol_lin_system(W,A,n,p,m)
        np.testing.assert_almost_equal(H_expected, H_obtained, 12)

    
# Roda testes para o modulo fatmatriz
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFatMatriz)
unittest.TextTestRunner(verbosity=2).run(suite1)