import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)
        self.assertEqual(min_jumps([2, 5, 0, 0, 3, 2, 0, 1, 2, 4, 2, 0], 13), 6)

    def test_edge_cases(self):
        self.assertEqual(min_jumps([0], 1), float('inf'))
        self.assertEqual(min_jumps([1, 0, 1, 0, 0], 5), float('inf'))
        self.assertEqual(min_jumps([1, 1, 1], 3), 0)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 5), 1)

    def test_boundary_conditions(self):
        self.assertEqual(min_jumps([], 0), 0)
        self.assertEqual(min_jumps([1], 1), 0)
        self.assertEqual(min_jumps([1, 1], 2), 1)
        self.assertEqual(min_jumps([1, 1, 1, 1], 4), 1)
