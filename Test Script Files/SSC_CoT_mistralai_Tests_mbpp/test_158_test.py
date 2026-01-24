import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 3), 1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 4), 0)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 5), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 2), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 3), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 4), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 1, 5), 0)
        self.assertEqual(min_Ops([], 0, 2), -1)
        self.assertEqual(min_Ops([1], 1, 1), 0)
        self.assertEqual(min_Ops([1], 2, 1), -1)

    def test_invalid_inputs(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], -1, 2), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, -1), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 0), -1)
