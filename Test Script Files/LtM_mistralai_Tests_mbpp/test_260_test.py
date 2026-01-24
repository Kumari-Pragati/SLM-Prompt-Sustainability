import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 3)
        self.assertEqual(newman_prime(3), 7)
        self.assertEqual(newman_prime(4), 15)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(newman_prime(-1), None)
        self.assertEqual(newman_prime(50), 317)
        self.assertEqual(newman_prime(100), 6775)
        self.assertEqual(newman_prime(200), 207975)

    def test_complex_scenarios(self):
        self.assertEqual(newman_prime(5), 21)
        self.assertEqual(newman_prime(10), 105)
        self.assertEqual(newman_prime(15), 561)
        self.assertEqual(newman_prime(20), 2741)
