import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_odd_length_sum(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 35)
        self.assertEqual(Odd_Length_Sum([10, 20, 30, 40, 50]), 1170)
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5, 6]), 70)
        self.assertEqual(Odd_Length_Sum([100, 200, 300, 400, 500]), 13575)
        self.assertEqual(Odd_Length_Sum([1, 2, 3]), 11)
