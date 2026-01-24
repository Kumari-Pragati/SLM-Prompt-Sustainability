import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_min_difference(self):
        self.assertEqual(min_difference([(1, 2), (3, 4), (5, 6)]), 1)
        self.assertEqual(min_difference([(10, 20), (30, 40), (50, 60)]), 10)
        self.assertEqual(min_difference([(-1, 1), (-2, 2), (-3, 3)]), 2)
        self.assertEqual(min_difference([(1, 1), (2, 2), (3, 3)]), 0)
        self.assertEqual(min_difference([(100, 200), (300, 400), (500, 600)]), 100)
