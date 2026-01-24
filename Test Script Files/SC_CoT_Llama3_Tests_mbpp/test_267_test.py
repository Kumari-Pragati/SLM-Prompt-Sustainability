import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 9)
        self.assertEqual(square_Sum(3), 36)

    def test_edge_cases(self):
        self.assertEqual(square_Sum(-1), 1)
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(1), 1)

    def test_boundary_cases(self):
        self.assertEqual(square_Sum(1e6), 1e12)

    def test_special_cases(self):
        self.assertEqual(square_Sum(0.5), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            square_Sum('a')
