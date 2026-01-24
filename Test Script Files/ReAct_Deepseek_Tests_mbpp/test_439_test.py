import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5]), 12345)

    def test_single_digit_case(self):
        self.assertEqual(multiple_to_single([5]), 5)

    def test_empty_list_case(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_negative_numbers_case(self):
        self.assertEqual(multiple_to_single([-1, -2, -3]), -123)

    def test_zero_in_list_case(self):
        self.assertEqual(multiple_to_single([0, 1, 2, 3]), 0123)

    def test_large_numbers_case(self):
        self.assertEqual(multiple_to_single([9, 8, 7, 6, 5, 4, 3, 2, 1]), 987654321)

    def test_mixed_positive_negative_case(self):
        self.assertEqual(multiple_to_single([-1, 2, -3, 4]), -1234)

    def test_mixed_positive_zero_negative_case(self):
        self.assertEqual(multiple_to_single([0, 1, -2, 3]), 0123)

    def test_mixed_numbers_case(self):
        self.assertEqual(multiple_to_single([10, 20, 30, 40, 50]), 1020304050)
