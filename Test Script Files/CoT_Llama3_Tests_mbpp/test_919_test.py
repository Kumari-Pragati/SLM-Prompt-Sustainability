import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_multiply_list_empty_list(self):
        self.assertEqual(multiply_list([]), 1)

    def test_multiply_list_single_element(self):
        self.assertEqual(multiply_list([5]), 5)

    def test_multiply_list_multiple_elements(self):
        self.assertEqual(multiply_list([1, 2, 3, 4, 5]), 120)

    def test_multiply_list_negative_numbers(self):
        self.assertEqual(multiply_list([-1, -2, -3, -4, -5]), -120)

    def test_multiply_list_mixed_positive_negative(self):
        self.assertEqual(multiply_list([1, -2, 3, -4, 5]), -24)

    def test_multiply_list_zero(self):
        self.assertEqual(multiply_list([0, 1, 2, 3, 4]), 0)

    def test_multiply_list_all_zeros(self):
        self.assertEqual(multiply_list([0, 0, 0, 0, 0]), 0)
