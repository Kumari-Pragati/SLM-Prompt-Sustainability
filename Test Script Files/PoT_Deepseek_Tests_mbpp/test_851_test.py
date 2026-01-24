import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSumOfInverseDivisors(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(4, 10), 2.5, places=2)
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(2, 3), 1.5, places=2)
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(1, 5), 5.0, places=2)

    def test_edge_cases(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(0, 10), 0.0, places=2)
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(1, 0), 0.0, places=2)

    def test_boundary_cases(self):
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(2147483647, 1), 0.47, places=2)
        self.assertAlmostEqual(Sum_of_Inverse_Divisors(2147483647, 2147483647), 1073741823.5, places=2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors("4", 10)
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors(4, "10")
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors("4", "10")
