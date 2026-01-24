import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)
        self.assertEqual(min_jumps([2, 5, 0, 0, 3, 2, 0, 1, 2, 4, 2, 0], 13), 6)

    def test_edge_cases(self):
        self.assertEqual(min_jumps([0], 1), 0)
        self.assertEqual(min_jumps([0, 0], 2), float('inf'))
        self.assertEqual(min_jumps([1, 2, 3, 4], 0), float('inf'))
        self.assertEqual(min_jumps([1, 2, 3, 4], 5), 1)
        self.assertEqual(min_jumps([1, 2, 3, 4], 6), float('inf'))

    def test_boundary_cases(self):
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 6), 1)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 4), 1)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 2), 3)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 1), 4)
