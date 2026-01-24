import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply_list([1, 2, 3, 4]), 24)

    def test_zero_in_list(self):
        self.assertEqual(multiply_list([1, 0, 3, 4]), 0)

    def test_empty_list(self):
        self.assertEqual(multiply_list([]), 1)

    def test_negative_numbers(self):
        self.assertEqual(multiply_list([-1, -2, -3]), 6)
