import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(remove_even([2]), [])

    def test_edge_case_all_even(self):
        self.assertEqual(remove_even([2, 4, 6, 8]), [])

    def test_edge_case_all_odd(self):
        self.assertEqual(remove_even([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_edge_case_mixed(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_edge_case_duplicates(self):
        self.assertEqual(remove_even([2, 2, 4, 4, 6, 6]), [])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(remove_even([-2, -4, -6, -8]), [])

    def test_edge_case_positive_and_negative_numbers(self):
        self.assertEqual(remove_even([-2, -4, 1, 3, 5, 6]), [1, 3, 5])
