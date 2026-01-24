import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(angle_complex(1, 2), cmath.phase(complex(3, 2)))

    def test_edge_case_zero_real(self):
        self.assertAlmostEqual(angle_complex(0, 2), cmath.phase(complex(2, 2)))

    def test_edge_case_zero_imaginary(self):
        self.assertAlmostEqual(angle_complex(2, 0), cmath.phase(complex(2, 0)))

    def test_edge_case_zero_both(self):
        self.assertAlmostEqual(angle_complex(0, 0), cmath.phase(complex(0, 0)))

    def test_edge_case_negative_real(self):
        self.assertAlmostEqual(angle_complex(-1, 2), cmath.phase(complex(-1, 2)))

    def test_edge_case_negative_imaginary(self):
        self.assertAlmostEqual(angle_complex(2, -2), cmath.phase(complex(2, -2)))

    def test_edge_case_negative_both(self):
        self.assertAlmostEqual(angle_complex(-1, -2), cmath.phase(complex(-1, -2)))

    def test_edge_case_large_real(self):
        self.assertAlmostEqual(angle_complex(100, 2), cmath.phase(complex(100, 2)))

    def test_edge_case_large_imaginary(self):
        self.assertAlmostEqual(angle_complex(2, 100), cmath.phase(complex(2, 100)))

    def test_edge_case_large_both(self):
        self.assertAlmostEqual(angle_complex(100, 100), cmath.phase(complex(100, 100)))

    def test_edge_case_small_real(self):
        self.assertAlmostEqual(angle_complex(0.1, 2), cmath.phase(complex(0.1, 2)))

    def test_edge_case_small_imaginary(self):
        self.assertAlmostEqual(angle_complex(2, 0.1), cmath.phase(complex(2, 0.1)))

    def test_edge_case_small_both(self):
        self.assertAlmostEqual(angle_complex(0.1, 0.1), cmath.phase(complex(0.1, 0.1)))

    def test_edge_case_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            angle_complex(0, 0)
