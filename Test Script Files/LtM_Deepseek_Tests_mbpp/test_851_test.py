import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(4, 10), 2.5, places=2)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(1, 1), 1.0, places=2)
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(0, 0), float('inf'), places=2)

    def test_edge_cases(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(0, 10), float('inf'), places=2)
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(10, 0), 0.0, places=2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors('a', 10)
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors(10, 'a')
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors('a', 'b')
