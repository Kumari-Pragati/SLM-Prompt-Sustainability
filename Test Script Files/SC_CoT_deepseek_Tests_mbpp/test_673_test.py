import unittest

from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(convert([1, 2, 3, 4, 5]), 12345)

    def test_single_digit(self):
        self.assertEqual(convert([5]), 5)

    def test_empty_list(self):
        self.assertEqual(convert([]), 0)

    def test_large_number(self):
        self.assertEqual(convert([9, 9, 9, 9, 9]), 99999)

    def test_zero_in_list(self):
        self.assertEqual(convert([0, 1, 2, 3, 4]), 1234)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            convert([-1, -2, -3])

    def test_non_integer_elements(self):
        with self.assertRaises(ValueError):
            convert([1, 2, '3', 4])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            convert("12345")
