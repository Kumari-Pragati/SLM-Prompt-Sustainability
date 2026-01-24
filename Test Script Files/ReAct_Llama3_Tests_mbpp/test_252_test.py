import unittest
from mbpp_252_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_convert_positive_numbers(self):
        self.assertEqual(convert([1, 2, 3]), [(1, 0), (2, 0), (3, 0)])

    def test_convert_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3]), [(-1, 0), (-2, 0), (-3, 0)])

    def test_convert_zero(self):
        self.assertEqual(convert([0]), [(0, 0)])

    def test_convert_complex_numbers(self):
        self.assertEqual(convert([1 + 2j, 2 - 3j, 3 + 4j]), [(1, 2), (2, -3), (3, 4)])

    def test_convert_empty_list(self):
        self.assertEqual(convert([]), [])

    def test_convert_non_numeric_input(self):
        with self.assertRaises(TypeError):
            convert(['a', 'b', 'c'])
