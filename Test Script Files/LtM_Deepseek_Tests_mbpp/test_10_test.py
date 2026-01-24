import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(small_nnum([3, 1, 2], 2), [1, 2])

    def test_empty_list(self):
        self.assertEqual(small_nnum([], 2), [])

    def test_single_element(self):
        self.assertEqual(small_nnum([5], 1), [5])

    def test_duplicate_elements(self):
        self.assertEqual(small_nnum([3, 1, 2, 1, 2], 2), [1, 2])

    def test_n_greater_than_list_length(self):
        self.assertEqual(small_nnum([3, 1, 2], 5), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(small_nnum([-3, -1, -2], 2), [-3, -2])

    def test_large_numbers(self):
        self.assertEqual(small_nnum([1000, 2000, 3000], 2), [1000, 2000])
