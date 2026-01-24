import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_Jumps(2, 3, 1), 2)
        self.assertEqual(min_Jumps(5, 5, 10), 2)
        self.assertEqual(min_Jumps(0, 10, 10), 1)
        self.assertEqual(min_Jumps(10, 0, 10), 1)
        self.assertEqual(min_Jumps(10, 10, 0), 0)
        self.assertEqual(min_Jumps(10, 10, 10), 1)
        self.assertEqual(min_Jumps(10, 10, 20), 1)
        self.assertEqual(min_Jumps(10, 10, 11), 2)

    def test_edge_cases(self):
        self.assertEqual(min_Jumps(0, 0, 0), 0)
        self.assertEqual(min_Jumps(0, 0, 1), 1)
        self.assertEqual(min_Jumps(0, 0, 2), 2)
        self.assertEqual(min_Jumps(1, 0, 0), 1)
        self.assertEqual(min_Jumps(0, 1, 0), 1)
        self.assertEqual(min_Jumps(0, 1, 1), 2)
        self.assertEqual(min_Jumps(1, 1, 0), 1)
        self.assertEqual(min_Jumps(1, 1, 1), 1)
        self.assertEqual(min_Jumps(1, 1, 2), 2)

    def test_error_cases(self):
        # Test with negative values
        self.assertEqual(min_Jumps(-1, -2, -3), 3)
        self.assertEqual(min_Jumps(-1, 2, -3), 3)
        self.assertEqual(min_Jumps(1, -2, -3), 3)
        self.assertEqual(min_Jumps(-1, -2, 3), 2)
        self.assertEqual(min_Jumps(1, -2, 3), 2)
        self.assertEqual(min_Jumps(-1, 2, 3), 2)
