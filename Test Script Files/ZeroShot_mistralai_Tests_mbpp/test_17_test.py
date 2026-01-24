import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_square_perimeter_positive(self):
        self.assertEqual(square_perimeter(3), 12)
        self.assertEqual(square_perimeter(4), 16)
        self.assertEqual(square_perimeter(5), 20)

    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_square_perimeter_negative(self):
        self.assertEqual(square_perimeter(-1), 4)
        self.assertEqual(square_perimeter(-2), 8)
        self.assertEqual(square_perimeter(-3), 12)
