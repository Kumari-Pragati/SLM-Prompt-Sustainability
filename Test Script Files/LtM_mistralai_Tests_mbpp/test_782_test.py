import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3]), 10)
        self.assertEqual(Odd_Length_Sum([4, 5, 6]), 32)
        self.assertEqual(Odd_Length_Sum([7, 8, 9]), 56)

    def test_edge_and_boundary(self):
        self.assertEqual(Odd_Length_Sum([]), 0)
        self.assertEqual(Odd_Length_Sum([0]), 1)
        self.assertEqual(Odd_Length_Sum([1]), 1)
        self.assertEqual(Odd_Length_Sum([2]), 3)
        self.assertEqual(Odd_Length_Sum([3]), 6)
        self.assertEqual(Odd_Length_Sum([4]), 10)
        self.assertEqual(Odd_Length_Sum([5]), 17)
        self.assertEqual(Odd_Length_Sum([6]), 26)

    def test_complex(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 65)
        self.assertEqual(Odd_Length_Sum([6, 7, 8, 9, 10]), 164)
        self.assertEqual(Odd_Length_Sum([11, 12, 13, 14, 15]), 295)
        self.assertEqual(Odd_Length_Sum([16, 17, 18, 19, 20]), 460)
