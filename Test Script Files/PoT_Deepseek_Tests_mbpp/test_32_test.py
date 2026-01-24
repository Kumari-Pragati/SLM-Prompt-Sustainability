import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_Prime_Factors(315), 7)
        self.assertEqual(max_Prime_Factors(100), 5)
        self.assertEqual(max_Prime_Factors(13), 13)

    def test_edge_cases(self):
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(1), -1)

    def test_boundary_cases(self):
        self.assertEqual(max_Prime_Factors(0), -1)
        self.assertEqual(max_Prime_Factors(1000000000000), 101)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_Prime_Factors("abc")
        with self.assertRaises(TypeError):
            max_Prime_Factors(None)
        with self.assertRaises(TypeError):
            max_Prime_Factors([1,2,3])
