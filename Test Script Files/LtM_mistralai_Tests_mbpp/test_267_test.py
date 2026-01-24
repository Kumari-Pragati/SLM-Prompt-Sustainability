import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 8)
        self.assertEqual(square_Sum(3), 30)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(100), 3383500)
        self.assertEqual(square_Sum(-1), -1)

    def test_complex_scenarios(self):
        self.assertEqual(square_Sum(42), 37764)
        self.assertEqual(square_Sum(1000), 3383500000)
        self.assertEqual(square_Sum(2147483647), 87178291877)
