import unittest
from mbpp_940_code import shift_down

class TestShiftDown(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(shift_down([3, 4, 1, 5, 2]), [3, 5, 1, 4, 2])
        self.assertEqual(shift_down([10, 9, 8, 7, 6]), [10, 8, 9, 7, 6])
        self.assertEqual(shift_down([1, 2, 3, 4, 5]), [1, 3, 2, 4, 5])

    def test_edge_case_single_element(self):
        self.assertEqual(shift_down([1]), [])

    def test_edge_case_empty_list(self):
        self.assertEqual(shift_down([]), [])

    def test_edge_case_single_pair(self):
        self.assertEqual(shift_down([1, 2]), [2, 1])

    def test_edge_case_two_pairs(self):
        self.assertEqual(shift_down([1, 2, 3, 4]), [1, 3, 2, 4])

    def test_edge_case_reverse_order(self):
        self.assertEqual(shift_down([5, 4, 3, 2, 1]), [5, 3, 4, 2, 1])

    def test_edge_case_all_same(self):
        self.assertEqual(shift_down([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])

    def test_corner_case_first_child_larger(self):
        self.assertEqual(shift_down([1, 2, 3, 3, 4]), [1, 3, 3, 2, 4])

    def test_corner_case_last_child_smaller(self):
        self.assertEqual(shift_down([1, 2, 3, 4, 1]), [1, 3, 2, 4, 1])
