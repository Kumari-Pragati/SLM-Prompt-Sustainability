import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(slope(1, 2, 3, 4), 1.0)

    def test_negative_slope(self):
        self.assertEqual(slope(3, 4, 1, 2), -1.0)

    def test_vertical_line(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 3)

    def test_same_points(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            slope('a', 2, 3, 4)
