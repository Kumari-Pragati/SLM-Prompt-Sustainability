import unittest
from mbpp_412_code import remove_odd

class TestRemoveOdd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5]), [2, 4])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_odd([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(remove_odd([2]), [2])

    def test_edge_case_all_odd(self):
        self.assertEqual(remove_odd([1, 3, 5, 7]), [])

    def test_edge_case_all_even(self):
        self.assertEqual(remove_odd([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_edge_case_mixed(self):
        self.assertEqual(remove_odd([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(remove_odd([-1, -2, -3, -4, -5]), [-2, -4])

    def test_edge_case_zero(self):
        self.assertEqual(remove_odd([0, 1, 2, 3, 4, 5]), [0, 2, 4])
