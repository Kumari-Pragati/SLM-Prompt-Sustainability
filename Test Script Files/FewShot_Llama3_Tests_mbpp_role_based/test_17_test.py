import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_negative_number(self):
        self.assertEqual(square_perimeter(-5), 20)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            square_perimeter('a')
