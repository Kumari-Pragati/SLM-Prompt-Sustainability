import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(multiple_to_single([1]), 1)

    def test_multiple_digits(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5]), 12345)

    def test_with_zero(self):
        self.assertEqual(multiple_to_single([0, 0, 0]), 0)

    def test_with_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3]), -123)

    def test_with_mixed_numbers(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 0, -1]), 1230-1)
