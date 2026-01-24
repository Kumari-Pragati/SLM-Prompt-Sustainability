import unittest
from mbpp_10_code import small_nnum

class TestSmallNNum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(small_nnum([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(small_nnum([5], 1), [5])

    def test_multiple_elements_list(self):
        self.assertEqual(small_nnum([5, 2, 8, 12, 3], 3), [2, 3, 5])

    def test_n_is_zero(self):
        self.assertEqual(small_nnum([5, 2, 8, 12, 3], 0), [])

    def test_n_is_greater_than_list_length(self):
        self.assertEqual(small_nnum([5, 2, 8, 12, 3], 10), [2, 3, 5, 8, 12])

    def test_negative_numbers(self):
        self.assertEqual(small_nnum([-5, -2, -8, -12, -3], 3), [-12, -8, -5])

    def test_positive_numbers(self):
        self.assertEqual(small_nnum([5, 2, 8, 12, 3], 3), [2, 3, 5])

    def test_mixed_numbers(self):
        self.assertEqual(small_nnum([-5, 2, -8, 12, -3], 3), [-8, 2, 3])
