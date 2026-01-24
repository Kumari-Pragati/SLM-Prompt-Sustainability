import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4]), 1234)

    def test_single_digit_case(self):
        self.assertEqual(multiple_to_single([5]), 5)

    def test_empty_list_case(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_negative_numbers_case(self):
        self.assertEqual(multiple_to_single([-1, -2, -3, -4]), -1234)

    def test_zero_in_list_case(self):
        self.assertEqual(multiple_to_single([0, 1, 2, 3]), 1230)

    def test_large_numbers_case(self):
        self.assertEqual(multiple_to_single([9, 9, 9, 9]), 9999)

    def test_mixed_numbers_case(self):
        self.assertEqual(multiple_to_single([1, 0, 2, 3]), 1023)

    def test_large_input_case(self):
        self.assertEqual(multiple_to_single(list(range(1, 10001))), 10000)
