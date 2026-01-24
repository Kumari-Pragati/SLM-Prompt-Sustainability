import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_sum_even_odd(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4, 5]), 6)
        self.assertEqual(sum_even_odd([2, 4, 6, 8, 10]), 20)
        self.assertEqual(sum_even_odd([1, 3, 5, 7, 9]), 10)
        self.assertEqual(sum_even_odd([-1, -3, -5, -7, -9]), -10)
        self.assertEqual(sum_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 25)
        self.assertEqual(sum_even_odd([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -25)
        self.assertEqual(sum_even_odd([]), -1)
        self.assertEqual(sum_even_odd([2]), 2)
        self.assertEqual(sum_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 30)
