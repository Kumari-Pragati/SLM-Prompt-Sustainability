import unittest
from mbpp_252_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_convert_positive_integer(self):
        self.assertEqual(convert([1, 2, 3]), [(1, 0), (2, 0), (3, 0)])

    def test_convert_negative_integer(self):
        self.assertEqual(convert([-1, -2, -3]), [(-1, 0), (-2, 0), (-3, 0)])

    def test_convert_positive_float(self):
        self.assertEqual(convert([1.0, 2.0, 3.0]), [(1.0, 0), (2.0, 0), (3.0, 0)])

    def test_convert_negative_float(self):
        self.assertEqual(convert([-1.0, -2.0, -3.0]), [(-1.0, 0), (-2.0, 0), (-3.0, 0)])

    def test_convert_mixed_numbers(self):
        self.assertEqual(convert([1, 2.0, -3]), [(1, 0), (2.0, 0), (-3, 0)])

    def test_convert_empty_list(self):
        self.assertEqual(convert([]), [])

    def test_convert_non_numeric_input(self):
        with self.assertRaises(TypeError):
            convert(['a', 'b', 'c'])
