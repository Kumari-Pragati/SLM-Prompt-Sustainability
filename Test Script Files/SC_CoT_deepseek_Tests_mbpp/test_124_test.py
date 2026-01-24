import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(angle_complex(1, 1), 0.7853981633974483)

    def test_boundary_case(self):
        self.assertAlmostEqual(angle_complex(0, 0), 0.0)

    def test_edge_case(self):
        self.assertAlmostEqual(angle_complex(1, 0), 0.0)
        self.assertAlmostEqual(angle_complex(0, 1), 1.5707963267948966)

    def test_negative_numbers(self):
        self.assertAlmostEqual(angle_complex(-1, -1), -2.356194490192345)

    def test_large_numbers(self):
        self.assertAlmostEqual(angle_complex(1000, 1000), 1.1071487177940904)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            angle_complex('a', 'b')
        with self.assertRaises(TypeError):
            angle_complex(1, 'b')
        with self.assertRaises(TypeError):
            angle_complex('a', 1)
