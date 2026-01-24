import unittest
from mbpp_851_code import Sum_of_Inverse_Divisors

class TestSum_of_Inverse_Divisors(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(Sum_of_Inverse_Divisors(10, 100), 10.0)

    def test_edge_cases(self):
        self.assertEqual(Sum_of_Inverse_Divisors(0, 100), 100.0)
        self.assertEqual(Sum_of_Inverse_Divisors(100, 0), 0.0)
        self.assertEqual(Sum_of_Inverse_Divisors(0, 0), 0.0)

    def test_special_cases(self):
        self.assertEqual(Sum_of_Inverse_Divisors(1, 1), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(2, 2), 1.0)
        self.assertEqual(Sum_of_Inverse_Divisors(3, 3), 1.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors('a', 100)
        with self.assertRaises(TypeError):
            Sum_of_Inverse_Divisors(10, 'a')
