import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_Inv_Count([1, 2, 3, 4], 4), 0)
        self.assertEqual(get_Inv_Count([4, 3, 2, 1], 4), 3)
        self.assertEqual(get_Inv_Count([1, 1, 1, 1], 4), 0)

    def test_edge_cases(self):
        self.assertEqual(get_Inv_Count([1, 2], 2), 1)
        self.assertEqual(get_Inv_Count([2, 1], 2), 1)
        self.assertEqual(get_Inv_Count([1], 1), 0)
        self.assertEqual(get_Inv_Count([], 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(get_Inv_Count([-1, 0, 1], 3), 1)
        self.assertEqual(get_Inv_Count([1, 0, -1], 3), 1)
        self.assertEqual(get_Inv_Count([-1, -1, -1], 3), 0)
        self.assertEqual(get_Inv_Count([1, 1, 1], 1), 0)

    def test_complex_cases(self):
        self.assertEqual(get_Inv_Count([1, 1, 2, 1, 2], 5), 2)
        self.assertEqual(get_Inv_Count([2, 2, 2, 1, 1], 5), 3)
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5], 5), 10)
        self.assertEqual(get_Inv_Count([5, 4, 3, 2, 1], 5), 15)
