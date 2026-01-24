import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(10, 2), 0.2)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(1, 1), 1.0)
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(0, 0), float('inf'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors('10', 2)
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors(10, '2')
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors('10', '2')
