import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_List(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])
        self.assertEqual(swap_List(['a', 'b', 'c']), ['c', 'b', 'a'])
        self.assertEqual(swap_List([True, False]), [False, True])
        self.assertEqual(swap_List([1]), [1])
        self.assertEqual(swap_List([]), [])
