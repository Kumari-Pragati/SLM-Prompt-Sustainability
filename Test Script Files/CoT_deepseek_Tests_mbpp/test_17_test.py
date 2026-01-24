import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_zero_input(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_negative_input(self):
        self.assertEqual(square_perimeter(-3), -12)

    def test_large_number(self):
        self.assertEqual(square_perimeter(10000), 40000)

    def test_non_integer_input(self):
        self.assertEqual(square_perimeter(3.5), 14)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            square_perimeter('a')

    def test_list_input(self):
        with self.assertRaises(TypeError):
            square_perimeter([1, 2, 3])
