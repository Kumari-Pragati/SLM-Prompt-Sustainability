import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 4)
        self.assertEqual(square_Sum(3), 9)
        self.assertEqual(square_Sum(4), 16)

    def test_edge_cases(self):
        self.assertEqual(square_Sum(-1), 0)
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(100), 338350)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            square_Sum('a')
        with self.assertRaises(TypeError):
            square_Sum(None)
