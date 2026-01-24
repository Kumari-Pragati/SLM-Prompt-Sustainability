import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):
    def test_square_perimeter_positive(self):
        self.assertEqual(square_perimeter(3), 12)
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(10), 40)

    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_square_perimeter_negative(self):
        self.assertEqual(square_perimeter(-1), 4)
        self.assertEqual(square_perimeter(-3), 12)

    def test_invalid_input(self):
        self.assertRaises(TypeError, square_perimeter, 'a string')
        self.assertRaises(TypeError, square_perimeter, 0.5)
