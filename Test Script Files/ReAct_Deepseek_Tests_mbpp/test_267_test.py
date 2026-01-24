import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 13)
        self.assertEqual(square_Sum(3), 34)

    def test_edge_cases(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(-1), 1)

    def test_large_numbers(self):
        self.assertEqual(square_Sum(10), 2670)
        self.assertEqual(square_Sum(100), 267000)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            square_Sum(1.5)

    def test_negative_integer_input(self):
        with self.assertRaises(ValueError):
            square_Sum(-1)
