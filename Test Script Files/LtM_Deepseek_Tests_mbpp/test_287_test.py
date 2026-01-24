import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 9)
        self.assertEqual(square_Sum(3), 36)

    def test_edge_conditions(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(10), 3850)

    def test_boundary_conditions(self):
        self.assertEqual(square_Sum(100), 338350)

    def test_complex_cases(self):
        self.assertEqual(square_Sum(1000), 33835000)
