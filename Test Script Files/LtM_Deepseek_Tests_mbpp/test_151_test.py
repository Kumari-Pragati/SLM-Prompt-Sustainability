import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertTrue(is_coprime(2, 3))
        self.assertTrue(is_coprime(5, 7))
        self.assertTrue(is_coprime(11, 13))

    # Test for edge and boundary conditions
    def test_boundary_conditions(self):
        self.assertTrue(is_coprime(1, 1))  # 1 and 1 are not coprime
        self.assertFalse(is_coprime(0, 0))  # Both 0 and 0 are not coprime
        self.assertTrue(is_coprime(0, 1))  # 0 and 1 are coprime
        self.assertTrue(is_coprime(1, 0))  # 1 and 0 are coprime

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertFalse(is_coprime(4, 6))  # 4 and 6 are not coprime
        self.assertFalse(is_coprime(8, 12))  # 8 and 12 are not coprime
        self.assertFalse(is_coprime(15, 15))  # 15 and 15 are not coprime
