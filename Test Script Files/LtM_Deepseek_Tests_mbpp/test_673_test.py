import unittest
from mbpp_673_code import convert

class TestConvertFunction(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(convert([1, 2, 3]), 123)
        self.assertEqual(convert([9, 8, 7]), 987)

    def test_single_digit_list(self):
        self.assertEqual(convert([5]), 5)

    def test_empty_list(self):
        self.assertEqual(convert([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3]), -123)

    def test_large_numbers(self):
        self.assertEqual(convert([9, 9, 9, 9, 9]), 99999)

    def test_mixed_numbers(self):
        self.assertEqual(convert([0, 1, 2, 3]), 123)
        self.assertEqual(convert([9, 0, 8, 7]), 987)

    def test_float_numbers(self):
        with self.assertRaises(TypeError):
            convert([1.1, 2.2, 3.3])

    def test_string_numbers(self):
        with self.assertRaises(TypeError):
            convert(["1", "2", "3"])
