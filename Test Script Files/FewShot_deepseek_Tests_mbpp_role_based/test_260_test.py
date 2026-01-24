import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 4)
        self.assertEqual(newman_prime(3), 10)
        self.assertEqual(newman_prime(4), 28)

    def test_boundary_conditions(self):
        self.assertEqual(newman_prime(5), 84)
        self.assertEqual(newman_prime(6), 244)
        self.assertEqual(newman_prime(7), 740)
        self.assertEqual(newman_prime(8), 2248)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            newman_prime('a')
        with self.assertRaises(TypeError):
            newman_prime(None)
        with self.assertRaises(TypeError):
            newman_prime([])
        with self.assertRaises(TypeError):
            newman_prime({})
