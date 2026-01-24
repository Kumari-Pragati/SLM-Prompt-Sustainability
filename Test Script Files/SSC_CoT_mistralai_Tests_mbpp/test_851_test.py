import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 35), 3.5)
        self.assertEqual(Sum_of_Inverse_Divisors(25, 156.25), 2.13)

    def test_edge_cases(self):
        self.assertEqual(Sum_of_Inverse_Divisors(1, 1), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(2, 1), 0.5)
        self.assertEqual(Sum_of_Inverse_Divisors(3, 1.5), 1.0)

    def test_boundary_conditions(self):
        self.assertEqual(Sum_of_Inverse_Divisors(4, 1.25), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(5, 2.0), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(6, 3.75), 1.25)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Sum_of_Inverse_Divisors, 'a', 1.25)
        self.assertRaises(TypeError, Sum_of_Inverse_Divisors, 1, 'b')
        self.assertRaises(ValueError, Sum_of_Inverse_Divisors, 0, 1.25)
        self.assertRaises(ValueError, Sum_of_Inverse_Divisors, 1, 0)
