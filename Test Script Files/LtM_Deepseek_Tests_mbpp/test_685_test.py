import unittest
from mbpp_685_code import sum_Of_Primes

class TestSumOfPrimes(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_Of_Primes(10), 17)
        self.assertEqual(sum_Of_Primes(20), 77)

    def test_edge_conditions(self):
        self.assertEqual(sum_Of_Primes(0), 0)
        self.assertEqual(sum_Of_Primes(1), 0)
        self.assertEqual(sum_Of_Primes(2), 2)

    def test_boundary_conditions(self):
        self.assertEqual(sum_Of_Primes(100), 1060)
        self.assertEqual(sum_Of_Primes(1000), 76127)

    def test_complex_cases(self):
        self.assertEqual(sum_Of_Primes(30), 173)
        self.assertEqual(sum_Of_Primes(50), 792)
