import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 13)
        self.assertEqual(square_Sum(3), 44)
        self.assertEqual(square_Sum(4), 105)
        self.assertEqual(square_Sum(5), 206)

    def test_boundary_conditions(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(100), 83205)

    def test_edge_cases(self):
        self.assertEqual(square_Sum(-1), 1)
        self.assertEqual(square_Sum(-10), 1049)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            square_Sum('a')
        with self.assertRaises(TypeError):
            square_Sum(None)
        with self.assertRaises(TypeError):
            square_Sum([1, 2, 3])
