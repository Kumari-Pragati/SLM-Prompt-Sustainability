import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(small_nnum([1,2,3,4,5,6,7,8,9,10], 3), [1,2,3])

    def test_edge_case_n_equal_to_list_length(self):
        self.assertEqual(small_nnum([1,2,3,4,5,6,7,8,9,10], 10), [1,2,3,4,5,6,7,8,9,10])

    def test_edge_case_n_greater_than_list_length(self):
        self.assertRaises(ValueError, small_nnum, [1,2,3,4,5,6,7,8,9,10], 11)

    def test_edge_case_n_zero(self):
        self.assertRaises(ValueError, small_nnum, [1,2,3,4,5,6,7,8,9,10], 0)

    def test_edge_case_n_negative(self):
        self.assertRaises(ValueError, small_nnum, [1,2,3,4,5,6,7,8,9,10], -1)

    def test_edge_case_empty_list(self):
        self.assertRaises(ValueError, small_nnum, [], 3)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(small_nnum([1,2,2,3,3,3,4,4,4,4], 3), [1,2,3])

    def test_edge_case_list_with_duplicates_and_n_equal_to_list_length(self):
        self.assertEqual(small_nnum([1,2,2,3,3,3,4,4,4,4], 10), [1,2,2,3,3,3,4,4,4,4])

    def test_edge_case_list_with_duplicates_and_n_greater_than_list_length(self):
        self.assertRaises(ValueError, small_nnum, [1,2,2,3,3,3,4,4,4,4], 11)

    def test_edge_case_list_with_duplicates_and_n_zero(self):
        self.assertRaises(ValueError, small_nnum, [1,2,2,3,3,3,4,4,4,4], 0)

    def test_edge_case_list_with_duplicates_and_n_negative(self):
        self.assertRaises(ValueError, small_nnum, [1,2,2,3,3,3,4,4,4,4], -1)
