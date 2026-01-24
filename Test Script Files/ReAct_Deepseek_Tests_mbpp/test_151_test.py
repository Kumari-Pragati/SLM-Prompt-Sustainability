import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_coprime(2, 3))
        self.assertTrue(is_coprime(5, 7))
        self.assertTrue(is_coprime(11, 13))

    def test_edge_cases(self):
        self.assertTrue(is_coprime(1, 1))  # 1 and 1 are not coprime, but they are the only pair where gcd(x, y) == 1
        self.assertFalse(is_coprime(0, 0))  # 0 and 0 are not coprime
        self.assertFalse(is_coprime(0, 1))  # 0 and any number is not coprime

    def test_explicitly_handled_error_cases(self):
        # The function does not handle any error cases, so we don't need to test them
        pass
