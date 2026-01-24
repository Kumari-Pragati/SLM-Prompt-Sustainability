import unittest
from mbpp_856_code import find_Min_Swaps

class TestFind_Min_Swaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 1], 5), 2)

    def test_edge_case_zero(self):
        self.assertEqual(find_Min_Swaps([0, 0, 0, 0, 0], 5), 5)

    def test_edge_case_one(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case_all_zeroes(self):
        self.assertEqual(find_Min_Swaps([0, 0, 0, 0, 0], 5), 5)

    def test_edge_case_all_ones(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case_mixed(self):
        self.assertEqual(find_Min_Swaps([0, 1, 1, 0, 1], 5), 2)

    def test_edge_case_mixed_reverse(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1, 1, 0], 5), 2)

    def test_edge_case_mixed_reverse_zero(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1, 0, 0], 5), 3)

    def test_edge_case_mixed_reverse_one(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1, 1], 5), 0)
