import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_min_jumps_basic(self):
        self.assertEqual(min_Jumps(3, 2, 1), 2)
        self.assertEqual(min_Jumps(2, 3, 1), 2)
        self.assertEqual(min_Jumps(4, 2, 1), 3)
        self.assertEqual(min_Jumps(2, 4, 1), 3)
        self.assertEqual(min_Jumps(1, 2, 1), 2)
        self.assertEqual(min_Jumps(2, 1, 1), 2)

    def test_min_jumps_edge_cases(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(1, 0, 1), 1)
        self.assertEqual(min_Jumps(0, 1, 1), 1)
        self.assertEqual(min_Jumps(1, 1, 0), 1)
        self.assertEqual(min_Jumps(1, 1, 1), 1)
