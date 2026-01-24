import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_Inv_Count([1, 20, 6, 4, 5], 5), 5)

    def test_edge_condition_empty_input(self):
        self.assertEqual(get_Inv_Count([], 0), 0)

    def test_edge_condition_single_element(self):
        self.assertEqual(get_Inv_Count([5], 1), 0)

    def test_edge_condition_sorted_input(self):
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5], 5), 0)

    def test_edge_condition_reverse_sorted_input(self):
        self.assertEqual(get_Inv_Count([5, 4, 3, 2, 1], 5), 10)

    def test_complex_input(self):
        self.assertEqual(get_Inv_Count([4, 3, 2, 1], 4), 6)
