import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_zero_count(self):
        self.assertEqual(zero_count([0, 1, 2, 3, 0]), 0.4)
        self.assertEqual(zero_count([1, 2, 3, 4, 5]), 0.0)
        self.assertEqual(zero_count([0, 0, 0, 0, 0]), 1.0)
        self.assertEqual(zero_count([0, 1, 0, 1, 0]), 0.4)
        self.assertEqual(zero_count([]), 0.0)
        self.assertEqual(zero_count([1]), 0.0)
        self.assertEqual(zero_count([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 1.0)
        self.assertEqual(zero_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0.0)
