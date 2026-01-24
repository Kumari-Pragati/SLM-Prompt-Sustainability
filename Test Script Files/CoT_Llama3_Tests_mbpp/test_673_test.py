import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(convert([1, 2, 3]), 123)

    def test_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3]), -123)

    def test_zero(self):
        self.assertEqual(convert([0]), 0)

    def test_single_digit(self):
        self.assertEqual(convert([1]), 1)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            convert([])

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            convert([1, 'a', 3])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            convert('abc')
