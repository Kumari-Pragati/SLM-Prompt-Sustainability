import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_min_difference(self):
        self.assertEqual(min_difference([(1, 3), (2, 4), (5, 7)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (4, 5)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17)]), 1)
        self.assertEqual(min_difference([(1, 2), (2, 3), (3