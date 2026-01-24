import unittest
from mbpp_32_code import max_Prime_Factors

class TestMaxPrimeFactors(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(max_Prime_Factors(315), 7)
        self.assertEqual(max_Prime_Factors(13), 13)
        self.assertEqual(max_Prime_Factors(100), 5)

    # Test for edge and boundary conditions
    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_Prime_Factors(2), 2)
        self.assertEqual(max_Prime_Factors(1), -1)
        self.assertEqual(max_Prime_Factors(0), -1)
        self.assertEqual(max_Prime_Factors(1000000007), 1000000007)

    # Test for more complex or corner cases
    def test_more_complex_cases(self):
        self.assertEqual(max_Prime_Factors(1000000000000000000), 1000000009)
        self.assertEqual(max_Prime_Factors(1000000000000000001), 1000000009)
