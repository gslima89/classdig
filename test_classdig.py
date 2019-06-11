
import unittest

import classdig.fatmatriz


class TestFatMatriz(unittest.TestCase):

    def test_c_s_1(self):
        c,s = classdig.fatmatriz._c_s(1,1)
        self.assertAlmostEqual(c,-0.707106781186547,15)
        self.assertAlmostEqual(s,0.707106781186547,15)
    
    def test_c_s_2(self):
        c,s = classdig.fatmatriz._c_s(-1,1)
        self.assertAlmostEqual(c,0.707106781186547,15)
        self.assertAlmostEqual(s,0.707106781186547,15)
    
    def test_c_s_3(self):
        c,s = classdig.fatmatriz._c_s(-3,5)
        self.assertAlmostEqual(c,0.514495755427527,15)
        self.assertAlmostEqual(s,0.857492925712544,15)

    def test_c_s_4(self):
        c,s = classdig.fatmatriz._c_s(2,-1)
        self.assertAlmostEqual(c,0.894427190999916,15)
        self.assertAlmostEqual(s,0.447213595499958,15)

    def test_c_s_5(self):
        c,s = classdig.fatmatriz._c_s(-2,-3)
        self.assertAlmostEqual(c,-0.554700196225229,15)
        self.assertAlmostEqual(s,0.832050294337844,15)


if __name__ == '__main__':
    unittest.main() 