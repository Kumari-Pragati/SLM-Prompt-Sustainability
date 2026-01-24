import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_cummulative_sum(self):
        self.assertEqual(cummulative_sum([[1, 2], [3, 4], [5, 6]]), 21)
        self.assertEqual(cummulative_sum([[1, 2, 3], [4, 5, 6]]), 21)
        self.assertEqual(cummulative_sum([[1, 2, 3, 4], [5, 6, 7, 8]]), 36)
        self.assertEqual(cummulative_sum([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]), 60)
        self.assertEqual(cummulative_sum([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]), 78)
        self.assertEqual(cummulative_sum([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]]), 105)
        self.assertEqual(cummulative_sum([[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]), 144)
        self.assertEqual(cummulative_sum([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18]]), 171)
        self.assertEqual(cummulative_sum([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]), 210)
