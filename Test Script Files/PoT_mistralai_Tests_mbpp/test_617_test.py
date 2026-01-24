import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_Jumps(1, 2, 1), 2)
        self.assertEqual(min_Jumps(2, 3, 2), 3)
        self.assertEqual(min_Jumps(4, 5, 1), 6)
        self.assertEqual(min_Jumps(5, 4, 1), 6)
        self.assertEqual(min_Jumps(1, 1, 1), 1)
        self.assertEqual(min_Jumps(0, 1, 0), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(1, 0, 1), 1)
        self.assertEqual(min_Jumps(1, 1, 0), 1)
        self.assertEqual(min_Jumps(-1, 1, 1), None)
        self.assertEqual(min_Jumps(1, -1, 1), None)
        self.assertEqual(min_Jumps(1, 1, -1), None)
