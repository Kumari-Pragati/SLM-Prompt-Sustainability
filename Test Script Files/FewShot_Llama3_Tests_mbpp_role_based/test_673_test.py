import unittest
from mbpp_673_code import convert

class TestConvert(unittest.TestCase):
    def test_convert_single_digit_list(self):
        self.assertEqual(convert([1]), 1)

    def test_convert_multiple_digit_list(self):
        self.assertEqual(convert([1, 2, 3]), 123)

    def test_convert_list_with_zero(self):
        self.assertEqual(convert([0, 1, 2]), 012)

    def test_convert_list_with_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3]), -123)

    def test_convert_list_with_empty(self):
        with self.assertRaises(ValueError):
            convert([])

    def test_convert_list_with_non_integer(self):
        with self.assertRaises(TypeError):
            convert([1, 'a', 3])
