import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSum_of_Inverse_Divisors(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 100), 10.0)
        self.assertEqual(Sum_of_Inverse_Divisors(5, 50), 10.0)
        self.assertEqual(Sum_of_Inverse_Divisors(20, 200), 10.0)

    def test_edge_cases(self):
        self.assertEqual(Sum_of_Inverse_Divisors(0, 0), 0.0)
        self.assertEqual(Sum_of_Inverse_Divisors(1, 1), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(100, 10000), 100.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors('a', 100)
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors(10, 'b')
