import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_inv_count([1, 20, 6, 4, 5], 5), 5)

    def test_empty_array(self):
        self.assertEqual(get_inv_count([], 0), 0)

    def test_single_element(self):
        self.assertEqual(get_inv_count([1], 1), 0)

    def test_sorted_array(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5), 0)

    def test_reverse_sorted_array(self):
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5), 10)

    def test_duplicate_elements(self):
        self.assertEqual(get_inv_count([2, 3, 8, 6, 2, 3, 5], 7), 5)

    def test_negative_elements(self):
        self.assertEqual(get_inv_count([-1, -2, -3, -4, -5], 5), 10)

    def test_large_array(self):
        self.assertEqual(get_inv_count(list(range(1000, 0, -1)), 1000), 499500)
