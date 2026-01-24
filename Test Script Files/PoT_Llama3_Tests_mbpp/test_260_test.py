import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 2)
        self.assertEqual(newman_prime(3), 6)
        self.assertEqual(newman_prime(4), 14)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(newman_prime(-1), 1)
        self.assertEqual(newman_prime(5), 22)
        self.assertEqual(newman_prime(6), 44)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            newman_prime('a')
        with self.assertRaises(TypeError):
            newman_prime(None)
