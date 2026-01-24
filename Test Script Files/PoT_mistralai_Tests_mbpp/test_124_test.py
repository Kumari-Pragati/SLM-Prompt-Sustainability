import unittest
from mbpp_124_code import angle_complex

class TestAngleComplex(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(angle_complex(1, 0), 0)
        self.assertAlmostEqual(angle_complex(0, 1), 90)
        self.assertAlmostEqual(angle_complex(1, 1), 45)
        self.assertAlmostEqual(angle_complex(-1, 1), 135)

    def test_negative_numbers(self):
        self.assertAlmostEqual(angle_complex(-1, -1), 225)
        self.assertAlmostEqual(angle_complex(-1, -2), 270)
        self.assertAlmostEqual(angle_complex(-2, -1), 315)

    def test_zero_arguments(self):
        with self.assertRaises(ValueError):
            angle_complex(0, 0)

    def test_complex_numbers(self):
        self.assertAlmostEqual(angle_complex(1+2j, 0), 63.43)
        self.assertAlmostEqual(angle_complex(0, 1+2j), 90 + 63.43)
