import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 0, 1], 6), 3)
        self.assertEqual(find_Min_Swaps([1, 0, 1, 0, 1, 0], 6), 3)
        self.assertEqual(find_Min_Swaps([0, 0, 0, 0, 0, 0], 6), 0)
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1, 1, 1], 6), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Min_Swaps([0], 1), 0)
        self.assertEqual(find_Min_Swaps([1], 1), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)

    def test_corner_case_all_zeros_except_one(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 0, 0, 0], 6), 1)
