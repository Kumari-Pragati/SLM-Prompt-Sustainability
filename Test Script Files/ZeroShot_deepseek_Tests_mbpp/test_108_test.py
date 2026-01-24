import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):

    def test_merge_sorted_list(self):
        self.assertEqual(merge_sorted_list([1, 3, 5], [2, 4, 6], [0, 7, 8]), [0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(merge_sorted_list([10, 20, 30], [5, 15, 25], [100, 200, 300]), [5, 10, 15, 20, 25, 30, 100, 200, 300])
        self.assertEqual(merge_sorted_list([], [], []), [])
        self.assertEqual(merge_sorted_list([1], [1], [1]), [1, 1, 1])
        self.assertEqual(merge_sorted_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
