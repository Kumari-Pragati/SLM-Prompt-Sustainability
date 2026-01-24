import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_swap_list(self):
        self.assertEqual(swap_List([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])
        self.assertEqual(swap_List([10, 20, 30, 40, 50]), [50, 20, 30, 40, 10])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd', 'e']), ['e', 'b', 'c', 'd', 'a'])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6]), [6, 2, 3, 4, 5, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7]), [7, 2, 3, 4, 5, 6, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8]), [8, 2, 3, 4, 5, 6, 7, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9]), [9, 2, 3, 4, 5, 6, 7, 8, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 2, 3, 4, 5, 6, 7, 8, 9, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), [12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), [16, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), [17, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,