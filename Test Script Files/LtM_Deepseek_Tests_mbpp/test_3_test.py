import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertFalse(is_not_prime(1))
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))
        self.assertFalse(is_not_prime(11))

    def test_edge_conditions(self):
        self.assertFalse(is_not_prime(0))
        self.assertFalse(is_not_prime(-1))
        self.assertFalse(is_not_prime(2))  # prime number

    def test_boundary_conditions(self):
        self.assertFalse(is_not_prime(4))  # divisible by 2
        self.assertTrue(is_not_prime(9))  # divisible by 3
        self.assertTrue(is_not_prime(10))  # divisible by 2 and 5

    def test_complex_cases(self):
        self.assertTrue(is_not_prime(15))  # divisible by 3 and 5
        self.assertTrue(is_not_prime(21))  # divisible by 3 and 7
        self.assertTrue(is_not_prime(35))  # divisible by 5 and 7
