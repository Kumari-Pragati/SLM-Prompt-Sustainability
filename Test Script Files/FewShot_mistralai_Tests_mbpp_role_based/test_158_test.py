import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 2), 1)
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 3), 0)
        self.assertEqual(min_Ops([1, 2, 3, 4], 4, 4), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_Ops([], 0, 1), -1)
        self.assertEqual(min_Ops([1], 1, 1), 0)
        self.assertEqual(min_Ops([1, 2, 3, 4], 1, 1), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4], 5, 2), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4], 1, 2), -1)
