import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            square_perimeter(-5)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            square_perimeter(5.5)

    def test_large_number(self):
        self.assertEqual(square_perimeter(10**10), 4*(10**10))
