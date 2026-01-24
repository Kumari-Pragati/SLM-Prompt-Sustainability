import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(Find_Min([1, 2, 3]), 1)
        self.assertEqual(Find_Min([-1, -2, -3]), -3)
        self.assertEqual(Find_Min([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(Find_Min([]), None)
        self.assertEqual(Find_Min([float('inf')]), float('inf'))
        self.assertEqual(Find_Min([float('-inf')]), float('-inf'))

    def test_complex_input(self):
        self.assertEqual(Find_Min([-1, 0, 1, -2, 2]), -2)
        self.assertEqual(Find_Min([-1, 0, 1, -2, 2, -1]), -1)
        self.assertEqual(Find_Min([-1, 0, 1, -2, 2, -1, 0]), -1)
