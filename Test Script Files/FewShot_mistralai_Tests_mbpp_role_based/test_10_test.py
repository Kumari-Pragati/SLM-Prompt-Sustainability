import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 2), [1, 2])
        self.assertEqual(small_nnum([10, 20, 30, 40, 50], 3), [10, 20, 30])

    def test_edge_case_empty_list(self):
        self.assertListEqual(small_nnum([], 1), [])

    def test_edge_case_single_element(self):
        self.assertEqual(small_nnum([1], 1), [1])

    def test_edge_case_single_element_n_greater_than_list_size(self):
        self.assertListEqual(small_nnum([1], 2), [1])

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            small_nnum([1, 2, 3], -1)
