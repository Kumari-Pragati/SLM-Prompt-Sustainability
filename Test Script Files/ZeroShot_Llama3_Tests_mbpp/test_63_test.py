import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_max_difference(self):
        self.assertEqual(max_difference([(1, 3), (2, 4), (5, 7)]), 2)
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 1)
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 3)]), 0)
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 4)]), 2)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16)]), 1)
        self.assertEqual(max_difference([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12