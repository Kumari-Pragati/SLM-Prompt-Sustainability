import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_normal(self):
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 2, 3, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd']), ['d', 'b', 'c', 'a'])

    def test_swap_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_swap_single_element_list(self):
        self.assertEqual(swap_List([1]), [1])
        self.assertEqual(swap_List(['a']), ['a'])

    def test_swap_negative_index(self):
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 2, 3, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd']), ['d', 'b', 'c', 'a'])
        self.assertEqual(swap_List([-1, -2, -3, -4]), [-4, -2, -3, -1])
        self.assertEqual(swap_List(['-a', '-b', '-c', '-d']), ['-d', '-b', '-c', '-a'])

    def test_swap_out_of_range_index(self):
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 2, 3, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd']), ['d', 'b', 'c', 'a'])
        self.assertEqual(swap_List([1, 2, 3, 4], 5), [1, 2, 3, 4])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd'], -1), ['a', 'b', 'c', 'd'])
