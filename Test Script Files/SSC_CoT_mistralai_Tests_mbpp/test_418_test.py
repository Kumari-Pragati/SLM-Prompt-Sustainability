import unittest
from mbpp_418_code import Find_Max

class TestFindMax(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(Find_Max([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(Find_Max([0, 0, 0]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Find_Max([]), None)
        self.assertEqual(Find_Max([1]), 1)
        self.assertEqual(Find_Max([-1]), -1)
        self.assertEqual(Find_Max([float('inf'), 1]), float('inf'))
        self.assertEqual(Find_Max([-float('inf'), -1]), -float('inf'))

    def test_special_input(self):
        self.assertEqual(Find_Max([float('nan'), float('nan')]), None)
        self.assertEqual(Find_Max([float('nan'), 1]), 1)
        self.assertEqual(Find_Max([1, float('nan')]), 1)
