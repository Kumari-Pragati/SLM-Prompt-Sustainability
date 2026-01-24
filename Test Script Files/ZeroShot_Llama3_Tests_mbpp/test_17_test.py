import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_square_perimeter_positive(self):
        self.assertEqual(square_perimeter(1), 4)

    def test_square_perimeter_negative(self):
        self.assertEqual(square_perimeter(-1), 4)

    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_square_perimeter_non_integer(self):
        self.assertAlmostEqual(square_perimeter(1.5), 6.0)

    def test_square_perimeter_non_numeric(self):
        with self.assertRaises(TypeError):
            square_perimeter('a')
