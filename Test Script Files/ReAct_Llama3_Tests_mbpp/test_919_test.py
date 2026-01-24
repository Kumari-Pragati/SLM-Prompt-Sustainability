import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(multiply_list([]), 1)

    def test_single_element_list(self):
        self.assertEqual(multiply_list([5]), 5)

    def test_multiple_elements_list(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)

    def test_negative_elements_list(self):
        self.assertEqual(multiply_list([-1, -2, -3]), -6)

    def test_mixed_elements_list(self):
        self.assertEqual(multiply_list([1, -2, 3, -4]), -6)

    def test_zero_in_list(self):
        self.assertEqual(multiply_list([0, 1, 2]), 0)

    def test_all_zeros_list(self):
        self.assertEqual(multiply_list([0, 0, 0]), 0)
