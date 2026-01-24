import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):
    def test_overlapping_lists(self):
        self.assertEqual(overlapping([1, 2, 3, 4], [4, 5, 6, 7]), 1)
        self.assertEqual(overlapping([1, 1, 2, 3, 4], [4, 5, 6, 7]), 1)
        self.assertEqual(overlapping([], []), 0)
        self.assertEqual(overlapping([1, 2, 3, 4], []), 0)
        self.assertEqual(overlapping([], [1, 2, 3, 4]), 0)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3, 4]), 1)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3, 5]), 0)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3, 5, 6]), 0)
        self.assertEqual(overlapping([1, 2, 3], [1, 2, 3, 5, 6, 7]), 0)
