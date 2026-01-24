import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):
    def test_square_perimeter_positive(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_square_perimeter_negative(self):
        with self.assertRaises(TypeError):
            square_perimeter(-5)

    def test_square_perimeter_non_numeric(self):
        with self.assertRaises(TypeError):
            square_perimeter('five')

    def test_square_perimeter_empty(self):
        with self.assertRaises(TypeError):
            square_perimeter(None)
