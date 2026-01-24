import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):

    def test_normal_case(self):
        self.assertAlmostEqual(angle_complex(3, 4), 1.2649444566406346)
        self.assertAlmostEqual(angle_complex(-3, 4), 5.264944456640634)
        self.assertAlmostEqual(angle_complex(0, 0), 0)

    def test_edge_cases(self):
        self.assertAlmostEqual(angle_complex(1e-5, 1e-5), 0)
        self.assertAlmostEqual(angle_complex(-1e-5, 1e-5), 3.141592653589793)
        self.assertAlmostEqual(angle_complex(1e5, 1e5), 0)
        self.assertAlmostEqual(angle_complex(-1e5, 1e5), 3.141592653589793)

    def test_negative_b(self):
        self.assertAlmostEqual(angle_complex(3, -4), 2.617993877991494)
        self.assertAlmostEqual(angle_complex(-3, -4), 6.261799387799149)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            angle_complex('a', 'b')
        with self.assertRaises(TypeError):
            angle_complex(1, 'b')
        with self.assertRaises(TypeError):
            angle_complex('a', 1j)
