import unittest
from591_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 2, 3, 1])
        self.assertEqual(swap_List([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(swap_List(['a', 'b', 'c', 'd']), ['d', 'b', 'c', 'a'])

    def test_edge_case_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(swap_List([1]), [1])

    def test_boundary_case_single_zero(self):
        self.assertEqual(swap_List([0]), [0])

    def test_boundary_case_single_negative(self):
        self.assertEqual(swap_List([-1]), [-1])

    def test_corner_case_mixed_types(self):
        self.assertEqual(swap_List([1, 'a', 2, 'b']), ['b', 'a', 2, 1])
