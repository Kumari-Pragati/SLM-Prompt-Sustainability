import unittest
from mbpp_625_code import len

class TestSwapList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 2, 3, 1])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd']), ['d', 'b', 'c', 'a'])

    def test_edge_case_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(swap_List([1]), [1])
        self.assertEqual(swap_List(['a']), ['a'])

    def test_boundary_case_zero_index(self):
        self.assertEqual(swap_List([0]), [0])

    def test_boundary_case_negative_index(self):
        self.assertEqual(swap_List([1, -1]), [-1, 1])

    def test_boundary_case_list_length_1(self):
        self.assertEqual(swap_List([1]), [1])
