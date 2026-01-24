import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_multiply_list_with_positive_numbers(self):
        self.assertEqual(multiply_list([1, 2, 3, 4]), 24)

    def test_multiply_list_with_negative_numbers(self):
        self.assertEqual(multiply_list([-1, -2, -3, -4]), -24)

    def test_multiply_list_with_zero(self):
        self.assertEqual(multiply_list([1, 2, 3, 0]), 0)

    def test_multiply_list_with_single_element(self):
        self.assertEqual(multiply_list([5]), 5)

    def test_multiply_list_with_empty_list(self):
        self.assertEqual(multiply_list([]), 1)
