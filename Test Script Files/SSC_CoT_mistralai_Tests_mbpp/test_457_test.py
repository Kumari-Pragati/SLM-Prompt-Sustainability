import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(Find_Min([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(Find_Min([0, 0, 0]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Find_Min([-9223372036854775808]), -9223372036854775808)
        self.assertEqual(Find_Min([9223372036854775807]), 9223372036854775807)
        self.assertEqual(Find_Min([1, 0, -1]), -1)
        self.assertEqual(Find_Min([-1, -1, -1]), -1)
        self.assertEqual(Find_Min([float('inf'), 1, -1]), -1)
        self.assertEqual(Find_Min([-1, float('inf'), 1]), -1)

    def test_empty_list(self):
        self.assertIsNone(Find_Min([]))

    def test_single_element_list(self):
        self.assertEqual(Find_Min([1]), 1)
        self.assertEqual(Find_Min([-1]), -1)
