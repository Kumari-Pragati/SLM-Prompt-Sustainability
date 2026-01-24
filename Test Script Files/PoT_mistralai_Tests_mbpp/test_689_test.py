import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)
        self.assertEqual(min_jumps([2, 5, 0, 3, 3, 3, 2, 0, 0], 9), 6)
        self.assertEqual(min_jumps([0, 0, 0, 0, 0, 0, 0, 0, 0], 9), float('inf'))

    def test_edge_case(self):
        self.assertEqual(min_jumps([1], 1), 0)
        self.assertEqual(min_jumps([1, 0], 2), 1)
        self.assertEqual(min_jumps([1, 1, 1, 1, 1], 5), 1)

    def test_corner_case(self):
        self.assertEqual(min_jumps([1, 0, 1, 0, 1, 0, 1, 0, 1], 9), 3)
        self.assertEqual(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1], 9), 1)
