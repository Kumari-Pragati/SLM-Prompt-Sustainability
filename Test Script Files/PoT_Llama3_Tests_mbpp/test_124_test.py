import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(angle_complex(1, 1), 0.7853981633974483)

    def test_edge_case_zero_real(self):
        self.assertAlmostEqual(angle_complex(0, 1), 1.5707963267948966)

    def test_edge_case_zero_imaginary(self):
        self.assertAlmostEqual(angle_complex(1, 0), 0.0)

    def test_edge_case_zero_both(self):
        self.assertAlmostEqual(angle_complex(0, 0), 0.0)

    def test_edge_case_negative_real(self):
        self.assertAlmostEqual(angle_complex(-1, 1), 4.712389770819075)

    def test_edge_case_negative_imaginary(self):
        self.assertAlmostEqual(angle_complex(1, -1), 4.712389770819075)

    def test_edge_case_negative_both(self):
        self.assertAlmostEqual(angle_complex(-1, -1), 4.712389770819075)

    def test_edge_case_positive_real(self):
        self.assertAlmostEqual(angle_complex(1, 1), 0.7853981633974483)

    def test_edge_case_positive_imaginary(self):
        self.assertAlmostEqual(angle_complex(1, 1), 0.7853981633974483)

    def test_edge_case_positive_both(self):
        self.assertAlmostEqual(angle_complex(1, 1), 0.7853981633974483)

    def test_edge_case_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            angle_complex(0, 0)
