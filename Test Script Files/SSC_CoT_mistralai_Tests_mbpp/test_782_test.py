import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 36)
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5]), -36)
        self.assertEqual(Odd_Length_Sum([0, 0, 0, 0, 0]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(Odd_Length_Sum([]), 0)
        self.assertEqual(Odd_Length_Sum([1]), 1)
        self.assertEqual(Odd_Length_Sum([1, 1]), 2)
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5, 6]), 121)
        self.assertEqual(Odd_Length_Sum([1000000000, 1000000000, 1000000000, 1000000000, 1000000000]), 80000000000)

    def test_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, 2, -3, 4, -5]), -13)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Odd_Length_Sum(1.5)
        with self.assertRaises(TypeError):
            Odd_Length_Sum("string")
        with self.assertRaises(TypeError):
            Odd_Length_Sum(None)
