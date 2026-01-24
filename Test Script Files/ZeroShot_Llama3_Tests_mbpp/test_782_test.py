import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOdd_Length_Sum(unittest.TestCase):

    def test_Odd_Length_Sum(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5]), -15)
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5, 6]), 21)
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5, -6]), -21)
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5, 6, 7]), 28)
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5, -6, -7]), -28)
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5, 6, 7, 8]), 36)
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5, -6, -7, -8]), -36)
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5, 6, 7, 8, 9]), 45)
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5, -6, -7, -8, -9]), -45)
