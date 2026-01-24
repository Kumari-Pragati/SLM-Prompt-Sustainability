import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3]), 10)

    def test_single_element(self):
        self.assertEqual(Odd_Length_Sum([5]), 5)

    def test_empty_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, -2, -3]), -4)

    def test_large_numbers(self):
        self.assertEqual(Odd_Length_Sum([1000, 2000, 3000]), 6000)

    def test_large_list(self):
        self.assertEqual(Odd_Length_Sum(list(range(1, 1001))), 500500)

    def test_odd_length_list(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 15)

    def test_even_length_list(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4]), 10)
