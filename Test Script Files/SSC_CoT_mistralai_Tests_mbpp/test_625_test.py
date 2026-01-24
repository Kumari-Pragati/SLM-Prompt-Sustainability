import unittest
from mbpp_625_code import range
from six.moves import xrange

from625_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_list_empty(self):
        self.assertEqual(swap_List([]), [])

    def test_swap_list_single_element(self):
        self.assertEqual(swap_List([1]), [1])

    def test_swap_list_normal(self):
        for i in range(1, 6):
            self.assertEqual(swap_List([i for j in range(i)]), [j for j in range(i, 0, -1)])

    def test_swap_list_large_list(self):
        large_list = [j for i in range(100) for j in range(i)]
        self.assertEqual(swap_List(large_list), large_list[::-1])

    def test_swap_list_negative_list(self):
        self.assertEqual(swap_List([-1, -2, -3]), [3, 2, 1])

    def test_swap_list_mixed_list(self):
        self.assertEqual(swap_List([0, 1, 2, 3, 4]), [4, 3, 2, 0, 1])

    def test_swap_list_list_with_zero(self):
        self.assertEqual(swap_List([0, 1, 2, 3]), [3, 2, 0, 1])

    def test_swap_list_list_with_floats(self):
        self.assertEqual(swap_List([1.1, 2.2, 3.3]), [3.3, 2.2, 1.1])

    def test_swap_list_list_with_strings(self):
        self.assertEqual(swap_List(['a', 'b', 'c']), ['c', 'b', 'a'])

    def test_swap_list_list_with_mixed_types(self):
        self.assertEqual(swap_List([1, 'a', 2, 'b']), ['b', 'a', 2, 1])
