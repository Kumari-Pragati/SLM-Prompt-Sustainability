import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(square_perimeter(3), 12)

    def test_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            square_perimeter(-1)

    def test_float(self):
        with self.assertRaises(TypeError):
            square_perimeter(3.14)

    def test_non_number(self):
        with self.assertRaises(TypeError):
            square_perimeter('abc')
