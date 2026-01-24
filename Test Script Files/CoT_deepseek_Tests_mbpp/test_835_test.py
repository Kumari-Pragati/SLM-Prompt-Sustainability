import unittest
from mbpp_835_code import slope

class TestSlopeFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(slope(1, 2, 4, 8), 2.0)

    def test_negative_slope(self):
        self.assertAlmostEqual(slope(4, 8, 1, 2), -2.0)

    def test_vertical_line(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 3)

    def test_same_points(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            slope("1", 2, 1, 3)
        with self.assertRaises(TypeError):
            slope(1, "2", 1, 3)
        with self.assertRaises(TypeError):
            slope(1, 2, "1", 3)
        with self.assertRaises(TypeError):
            slope(1, 2, 1, "3")
