import unittest
from mbpp_151_code import is_coprime

class TestIsCoprime(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(is_coprime(25, 13))
        self.assertTrue(is_coprime(33, 29))

    def test_edge_cases(self):
        self.assertTrue(is_coprime(5, 7))  # smallest coprime pair
        self.assertTrue(is_coprime(99, 101))  # large coprime pair
        self.assertTrue(is_coprime(2**31 - 1, 2**30 + 1))  # largest known coprime pair

    def test_boundary(self):
        self.assertFalse(is_coprime(0, 1))
        self.assertFalse(is_coprime(1, 0))
        self.assertFalse(is_coprime(1, 1))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_coprime, 'a', 'b')
        self.assertRaises(TypeError, is_coprime, 1.0, 2.0)
        self.assertRaises(TypeError, is_coprime, [1, 2], [3, 4])
