import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 0], 5), 3)

    def test_all_zeros(self):
        self.assertEqual(find_Min_Swaps([0] * 10, 10), 10)

    def test_all_ones(self):
        self.assertEqual(find_Min_Swaps([1] * 10, 10), 0)

    def test_single_element(self):
        self.assertEqual(find_Min_Swaps([0], 1), 0)
        self.assertEqual(find_Min_Swaps([1], 1), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)

    def test_edge_case_single_zero(self):
        self.assertEqual(find_Min_Swaps([0], 1), 0)

    def test_edge_case_single_one(self):
        self.assertEqual(find_Min_Swaps([1], 1), 0)
