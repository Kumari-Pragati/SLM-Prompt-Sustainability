import unittest
from mbpp_252_code import convert

class TestConvert(unittest.TestCase):
    def test_convert_positive_numbers(self):
        self.assertEqual(convert([1, 2, 3]), [(1, 0), (2, 0), (3, 0)])

    def test_convert_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3]), [(-1, 0), (-2, 0), (-3, 0)])

    def test_convert_zero(self):
        self.assertEqual(convert([0]), [(0, 0)])

    def test_convert_empty_list(self):
        self.assertEqual(convert([]), [])

    def test_convert_non_numeric_input(self):
        with self.assertRaises(TypeError):
            convert(['a', 'b', 'c'])
