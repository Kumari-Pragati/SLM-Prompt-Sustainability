import unittest
from mbpp_835_code import slope

class TestSlopeFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(slope(1, 2, 4, 8), 2.0)

    def test_negative_slope(self):
        self.assertAlmostEqual(slope(4, 8, 1, 2), -2.0)

    def test_zero_slope(self):
        self.assertEqual(slope(1, 2, 1, 3), 0.0)

    def test_vertical_line(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 1)

    def test_same_points(self):
        self.assertIsNone(slope(1, 2, 1, 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            slope('a', 2, 1, 2)
