import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_min_jumps(self):
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)
        self.assertEqual(min_jumps([1, 1, 2, 3, 2], 5), 3)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(min_jumps([0, 1, 2, 3, 4], 5), float('inf'))
        self.assertEqual(min_jumps([1, 1, 1, 1, 1], 5), 4)
        self.assertEqual(min_jumps([1, 2, 3, 0, 4], 5), float('inf'))
        self.assertEqual(min_jumps([1, 1, 1, 1, 0], 5), float('inf'))
        self.assertEqual(min_jumps([1, 1, 1, 1, 1, 1], 6, ), 5)
        self.assertEqual(min_jumps([1, 1, 1, 1, 1, 1, 1], 7), 6)
        self.assertEqual(min_jumps([1, 1, 1, 1, 1, 1, 1, 1], 8), 7)
        self.assertEqual(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1], 9), 8)
        self.assertEqual(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10), 9)
