import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):

    def test_min_jumps(self):
        self.assertEqual(min_jumps([1, 3, 6, 3, 2, 3, 6, 8, 9, 5], 10), 3)
        self.assertEqual(min_jumps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10), 10)
        self.assertEqual(min_jumps([2, 3, 1, 1, 4], 5), 2)
        self.assertEqual(min_jumps([0], 1), float('inf'))
        self.assertEqual(min_jumps([2, 3, 0, 1, 4], 5), 2)
