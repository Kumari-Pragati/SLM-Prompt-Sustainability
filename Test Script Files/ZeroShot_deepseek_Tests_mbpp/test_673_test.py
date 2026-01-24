import unittest
from mbpp_673_code import convert

class TestConvert(unittest.TestCase):

    def test_convert_positive_numbers(self):
        self.assertEqual(convert([1, 2, 3]), 123)
        self.assertEqual(convert([9, 8, 7]), 987)
        self.assertEqual(convert([1, 0, 0, 0]), 1000)

    def test_convert_negative_numbers(self):
        self.assertEqual(convert([-1, -2, -3]), -123)
        self.assertEqual(convert([-9, -8, -7]), -987)
        self.assertEqual(convert([-1, 0, 0, 0]), -1000)

    def test_convert_mixed_numbers(self):
        self.assertEqual(convert([1, 2, 3, 4, 5]), 12345)
        self.assertEqual(convert([-1, -2, -3, -4, -5]), -12345)
        self.assertEqual(convert([0, 0, 0, 0, 0]), 0)

    def test_convert_empty_list(self):
        self.assertEqual(convert([]), 0)

    def test_convert_single_digit_numbers(self):
        self.assertEqual(convert([5]), 5)
        self.assertEqual(convert([0]), 0)
        self.assertEqual(convert([9]), 9)
