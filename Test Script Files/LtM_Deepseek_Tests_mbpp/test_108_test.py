import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6], [0, 7, 8]), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_edge_conditions(self):
        self.assertEqual(merge_sorted_list([], [], []), [])
        self.assertEqual(merge_sorted_list([1], [], []), [1])
        self.assertEqual(merge_sorted_list([], [2], []), [2])
        self.assertEqual(merge_sorted_list([], [], [3]), [3])

    def test_boundary_conditions(self):
        self.assertEqual(merge_sorted_list([1], [1], [1]), [1, 1, 1])
        self.assertEqual(merge_sorted_list([1, 2, 3], [1, 2, 3], [1, 2, 3]), [1, 1, 1, 2, 2, 2, 3, 3, 3])

    def test_complex_cases(self):
        self.assertEqual(merge_sorted_list([10, 20, 30], [5, 15, 25], [1, 9, 11]), [1, 5, 9, 10, 11, 15, 20, 25, 30])
