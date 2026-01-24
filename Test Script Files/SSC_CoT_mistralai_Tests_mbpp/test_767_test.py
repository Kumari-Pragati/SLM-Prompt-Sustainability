import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 3), 2)
        self.assertEqual(get_Pairs_Count([10, 15, 3, 7, 8, 9], 6, 23), 1)

    def test_edge_cases(self):
        self.assertEqual(get_Pairs_Count([], 0, 10), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 1, 10), 0)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 6, 6), 1)
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 7), 0)

    def test_boundary_conditions(self):
        self.assertEqual(get_Pairs_Count([0, 0], 2, 0), 1)
        self.assertEqual(get_Pairs_Count([-1, -1], 2, 0), 1)
        self.assertEqual(get_Pairs_Count([1, 1], 2, 2), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_Pairs_Count, [1, 2, 3], 'a', 6)
        self.assertRaises(TypeError, get_Pairs_Count, [1, 2, 3], 5, 'a')
