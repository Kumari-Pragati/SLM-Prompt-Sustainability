import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_List_simple(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])

    def test_swap_List_edge(self):
        self.assertEqual(swap_List([1]), [1])
        self.assertEqual(swap_List([]), [])

    def test_swap_List_boundary(self):
        self.assertEqual(swap_List([1, 2]), [2, 1])
        self.assertEqual(swap_List([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])

    def test_swap_List_complex(self):
        self.assertEqual(swap_List(['a', 'b', 'c']), ['c', 'b', 'a'])
        self.assertEqual(swap_List([1, 'a', True]), [True, 'a', 1])
