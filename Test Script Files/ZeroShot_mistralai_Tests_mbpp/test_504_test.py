import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_sum_of_series_for_small_numbers(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 8)
        self.assertEqual(sum_Of_Series(3), 81)
        self.assertEqual(sum_Of_Series(4), 274)
        self.assertEqual(sum_Of_Series(5), 7295)

    def test_sum_of_series_for_large_numbers(self):
        self.assertEqual(sum_Of_Series(10), 1000005)
        self.assertEqual(sum_Of_Series(20), 40000100)
        self.assertEqual(sum_Of_Series(30), 1800003000)
        self.assertEqual(sum_Of_Series(40), 8400006400)
        self.assertEqual(sum_Of_Series(50), 362500002500)
