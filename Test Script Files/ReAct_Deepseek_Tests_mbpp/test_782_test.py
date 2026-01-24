import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(Odd_Length_Sum(arr), 45)

    def test_single_element(self):
        arr = [1]
        self.assertEqual(Odd_Length_Sum(arr), 1)

    def test_empty_array(self):
        arr = []
        self.assertEqual(Odd_Length_Sum(arr), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(Odd_Length_Sum(arr), -45)

    def test_large_numbers(self):
        arr = [1000, 2000, 3000, 4000, 5000]
        self.assertEqual(Odd_Length_Sum(arr), 45000)

    def test_large_array(self):
        arr = list(range(1, 1001))
        self.assertEqual(Odd_Length_Sum(arr), sum(arr))

    def test_array_with_zero(self):
        arr = [0, 1, 2, 3, 4, 5]
        self.assertEqual(Odd_Length_Sum(arr), 15)
