import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_sum_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(max_sum_list([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(max_sum_list([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_list([-1, -2, -3]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(max_sum_list([1, -2, 3, -4, 5]), 10)

    def test_list_with_zero(self):
        self.assertEqual(max_sum_list([0, 1, 2, 3]), 6)

    def test_list_with_only_zero(self):
        self.assertEqual(max_sum_list([0, 0, 0]), 0)

    def test_list_with_only_negative_numbers(self):
        self.assertEqual(max_sum_list([-1, -2, -3]), -1)

    def test_list_with_only_large_numbers(self):
        self.assertEqual(max_sum_list([1000000, 2000000, 3000000]), 6000000)

    def test_list_with_only_small_numbers(self):
        self.assertEqual(max_sum_list([-1000000, -2000000, -3000000]), -3000000)

    def test_list_with_duplicates(self):
        self.assertEqual(max_sum_list([1, 1, 2, 3]), 5)
