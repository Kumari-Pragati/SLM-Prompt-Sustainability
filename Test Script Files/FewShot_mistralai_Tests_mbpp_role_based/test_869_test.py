import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_list_range([(1, 2), (3, 4), (5, 6)], 3, 5), [(3, 4)])
        self.assertEqual(remove_list_range([(0, 0), (1, 1), (2, 2)], 1, 2), [(1, 1)])
        self.assertEqual(remove_list_range([(0, 0), (1, 1), (2, 2)], 0, 1), [(0, 0)])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(remove_list_range([(0, 0)], 0, 0), [(0, 0)])
        self.assertEqual(remove_list_range([(0, 0)], 1, 0), [])
        self.assertEqual(remove_list_range([(0, 0)], -1, 0), [])
        self.assertEqual(remove_list_range([(0, 0)], 0, -1), [])
        self.assertEqual(remove_list_range([(0, 0)], -1, -1), [(0, 0)])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, remove_list_range, [(1, 2)], "a", "b")
        self.assertRaises(TypeError, remove_list_range, [(1, 2)], 3.5, 5)
        self.assertRaises(TypeError, remove_list_range, [(1, 2)], 3, "5")
