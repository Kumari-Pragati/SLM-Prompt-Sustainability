import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 9)
        self.assertEqual(square_Sum(3), 36)

    def test_edge(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(-1), 0)

    def test_negative(self):
        self.assertEqual(square_Sum(-2), 0)
        self.assertEqual(square_Sum(-3), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            square_Sum(1.5)

    def test_large(self):
        self.assertEqual(square_Sum(100), 1005001)

    def test_zero(self):
        self.assertEqual(square_Sum(0), 0)
