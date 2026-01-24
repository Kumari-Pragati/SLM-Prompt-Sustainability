import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):

    def test_zero_angle(self):
        self.assertEqual(angle_complex(1, 0), 0)

    def test_positive_angle(self):
        self.assertAlmostEqual(angle_complex(1, 1), math.pi / 4, delta=0.01)

    def test_negative_angle(self):
        self.assertAlmostEqual(angle_complex(-1, 1), -math.pi / 4, delta=0.01)

    def test_complex_number(self):
        self.assertAlmostEqual(angle_complex(1, -2), math.atan2(-2, 1), delta=0.01)
