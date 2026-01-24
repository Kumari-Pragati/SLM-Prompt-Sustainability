import unittest

from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 4)
        self.assertEqual(newman_prime(3), 10)
        self.assertEqual(newman_prime(4), 26)

    def test_edge_cases(self):
        self.assertEqual(newman_prime(-1), 1)
        self.assertEqual(newman_prime(-10), 1)
        self.assertEqual(newman_prime(5), 166)
        self.assertEqual(newman_prime(10), 1048576)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            newman_prime('a')
        with self.assertRaises(TypeError):
            newman_prime(None)
        with self.assertRaises(TypeError):
            newman_prime([1, 2, 3])
