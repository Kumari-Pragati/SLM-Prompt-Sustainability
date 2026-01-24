import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_Jumps(1, 2, 3), 2)
        self.assertEqual(min_Jumps(5, 10, 15), 3)
        self.assertEqual(min_Jumps(0, 10, 10), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(0, 10, 0), 0)
        self.assertEqual(min_Jumps(10, 0, 10), 1)
        self.assertEqual(min_Jumps(10, 10, 20), 2)

    def test_corner_cases(self):
        self.assertEqual(min_Jumps(10, 10, 10), 1)
        self.assertEqual(min_Jumps(10, 10, 9), 2)
        self.assertEqual(min_Jumps(10, 10, 11), 2)
        self.assertEqual(min_Jumps(10, 10, 100), 3)
