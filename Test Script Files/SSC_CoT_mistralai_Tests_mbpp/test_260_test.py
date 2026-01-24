import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 3)
        self.assertEqual(newman_prime(3), 7)
        self.assertEqual(newman_prime(4), 15)
        self.assertEqual(newman_prime(5), 31)
        self.assertEqual(newman_prime(6), 63)
        self.assertEqual(newman_prime(7), 127)
        self.assertEqual(newman_prime(8), 255)
        self.assertEqual(newman_prime(9), 511)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(newman_prime(-1), None)
        self.assertEqual(newman_prime(100), 32767)
        self.assertEqual(newman_prime(1000), 1048575)
        self.assertEqual(newman_prime(2 ** 31 - 1), 2147483647)
        self.assertEqual(newman_prime(2 ** 31), None)
