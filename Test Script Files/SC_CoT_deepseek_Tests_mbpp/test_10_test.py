import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 0), [])

    def test_edge_case_n_equals_length_of_list(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_edge_case_n_greater_than_length_of_list(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 10), [1, 2, 3, 4, 5])

    def test_edge_case_n_less_than_zero(self):
        with self.assertRaises(ValueError):
            small_nnum([1, 2, 3, 4, 5], -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(small_nnum([], 3), [])

    def test_special_case_duplicate_elements(self):
        self.assertEqual(small_nnum([1, 2, 2, 3, 4, 5], 3), [1, 2, 2])

    def test_special_case_negative_numbers(self):
        self.assertEqual(small_nnum([-5, -3, -1, 0, 2, 4], 3), [-5, -3, -1])
