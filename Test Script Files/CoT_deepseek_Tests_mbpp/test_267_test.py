import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 13)
        self.assertEqual(square_Sum(3), 44)

    def test_zero_input(self):
        self.assertEqual(square_Sum(0), 0)

    def test_negative_input(self):
        self.assertEqual(square_Sum(-1), 1)
        self.assertEqual(square_Sum(-2), -13)
        self.assertEqual(square_Sum(-3), -44)

    def test_large_input(self):
        self.assertEqual(square_Sum(10), 2670)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            square_Sum('a')
        with self.assertRaises(TypeError):
            square_Sum(None)
        with self.assertRaises(TypeError):
            square_Sum([])
