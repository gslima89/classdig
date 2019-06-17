
import unittest

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

    def test_sol_lin_system_1(self):
        n,p,m = 3,2,3
        A = [[0.3, 0.6, 0.0],[0.5, 0.0, 1.0],[0.4, 0.8, 0.0]]
        W = [[0.6,0],[0,1],[0.8,0]]
        H_expected = [[0.5, 1.0, 0.0], [0.5, 0.0, 1.0]]
        H_obtained = fatmatriz.sol_lin_system(W,A,n,p,m)
        self.assertAlmostEqual(H_expected, H_obtained, 15)


# Roda testes para o modulo fatmatriz
suite = unittest.TestLoader().loadTestsFromTestCase(TestFatMatriz)
unittest.TextTestRunner(verbosity=2).run(suite)

#TODO: Fazer testes para o modulo helper