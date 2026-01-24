import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(min_Jumps(1, 2, 1), 2)
        self.assertEqual(min_Jumps(2, 1, 1), 2)
        self.assertEqual(min_Jumps(3, 4, 1), 4)
        self.assertEqual(min_Jumps(4, 3, 1), 4)

    def test_edge_cases(self):
        self.assertEqual(min_Jumps(0, 1, 1), 0)
        self.assertEqual(min_Jumps(1, 0, 1), 0)
        self.assertEqual(min_Jumps(1, 1, 0), 0)
        self.assertEqual(min_Jumps(1, 1, 2), 2)
        self.assertEqual(min_Jumps(2, 1, 2), 3)
        self.assertEqual(min_Jumps(2, 2, 2), 2)

    def test_boundary_conditions(self):
        self.assertEqual(min_Jumps(1, 2, 2), 2)
        self.assertEqual(min_Jumps(2, 1, 2), 3)
        self.assertEqual(min_Jumps(2147483647, 2147483647, 1), 2147483647)
        self.assertEqual(min_Jumps(2147483647, 2147483647, 2147483647), 1)
