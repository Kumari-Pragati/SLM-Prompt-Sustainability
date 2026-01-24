import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(Sum_of_Inverse_Divisors(4, 2), 1.5)
        self.assertEqual(Sum_of_Inverse_Divisors(9, 3), 3.0)

    def test_edge_case(self):
        self.assertEqual(Sum_of_Inverse_Divisors(1, 1), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(2, 1), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(3, 1), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(4, 0), 0.0)
        self.assertEqual(Sum_of_Inverse_Divisors(0, 1), 0.0)
        self.assertEqual(Sum_of_Inverse_Divisors(100, 100), 100.0)

    def test_complex_case(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(12, 6), 2.33)
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(1000, 333.33), 333.33)
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(2000000000, 1000000000.5), 1000000000.5)
