import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_sum_of_series(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 28)
        self.assertEqual(sum_Of_Series(3), 109)
        self.assertEqual(sum_Of_Series(4), 216)
        self.assertEqual(sum_Of_Series(5), 377)
        self.assertEqual(sum_Of_Series(6), 588)
        self.assertEqual(sum_Of_Series(7), 833)
        self.assertEqual(sum_Of_Series(8), 1080)
        self.assertEqual(sum_Of_Series(9), 1332)
        self.assertEqual(sum_Of_Series(10), 1584)

    def test_sum_of_series_edge_cases(self):
        self.assertEqual(sum_Of_Series(0), 0)
        self.assertEqual(sum_Of_Series(-1), 0)
