import unittest
from mbpp_617_code import min_Jumps

class TestMinJumps(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_Jumps(1, 2, 3), 1.0)
        self.assertEqual(min_Jumps(2, 1, 3), 1.0)
        self.assertEqual(min_Jumps(3, 2, 1), 1.0)
        self.assertEqual(min_Jumps(1, 1, 1), 0)
        self.assertEqual(min_Jumps(1, 2, 0), 0)
        self.assertEqual(min_Jumps(1, 2, 1), 1)

    def test_edge(self):
        self.assertEqual(min_Jumps(1, 2, 1), 1)
        self.assertEqual(min_Jumps(1, 2, 2), 1)
        self.assertEqual(min_Jumps(1, 2, 3), 1.0)
        self.assertEqual(min_Jumps(1, 1, 1), 0)
        self.assertEqual(min_Jumps(1, 1, 0), 0)

    def test_complex(self):
        self.assertEqual(min_Jumps(1, 3, 4), 1.0)
        self.assertEqual(min_Jumps(2, 3, 4), 1.0)
        self.assertEqual(min_Jumps(3, 4, 5), 1.0)
        self.assertEqual(min_Jumps(4, 5, 6), 1.0)
