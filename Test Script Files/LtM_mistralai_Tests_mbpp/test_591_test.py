import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])
        self.assertEqual(swap_List([4, 5, 6]), [6, 5, 4])

    def test_edge_cases(self):
        self.assertEqual(swap_List([1]), [1])
        self.assertEqual(swap_List([1, 2]), [2, 1])
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_complex_cases(self):
        self.assertEqual(swap_List([0, 1, 2]), [2, 1, 0])
        self.assertEqual(swap_List([-1, 0, 1]), [1, 0, -1])
        self.assertEqual(swap_List([1, 'a', 3]), ['a', 1, 3])
