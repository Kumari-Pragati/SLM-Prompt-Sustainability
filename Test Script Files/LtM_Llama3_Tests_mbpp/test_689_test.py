import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_jumps([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_edge(self):
        self.assertEqual(min_jumps([1], 1), 0)
        self.assertEqual(min_jumps([1, 2], 2), 1)
        self.assertEqual(min_jumps([1, 2, 3], 3), 2)
        self.assertEqual(min_jumps([1, 2, 3, 4], 4), 3)
        self.assertEqual(min_jumps([1, 2, 3, 4, 5, 6], 6), 5)

    def test_invalid(self):
        with self.assertRaises(IndexError):
            min_jumps([], 0)
        with self.assertRaises(IndexError):
            min_jumps([1, 2, 3], 0)
        with self.assertRaises(IndexError):
            min_jumps([1, 2, 3, 4, 5, 6], -1)
