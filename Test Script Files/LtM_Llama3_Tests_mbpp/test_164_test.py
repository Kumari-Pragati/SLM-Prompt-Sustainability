import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertTrue(areEquivalent(1, 1))
        self.assertTrue(areEquivalent(2, 2))
        self.assertTrue(areEquivalent(3, 3))

    def test_edge_cases(self):
        self.assertTrue(areEquivalent(1, 2))
        self.assertTrue(areEquivalent(2, 4))
        self.assertTrue(areEquivalent(3, 6))

    def test_divisible_numbers(self):
        self.assertTrue(areEquivalent(4, 6))
        self.assertTrue(areEquivalent(6, 8))
        self.assertTrue(areEquivalent(8, 12))

    def test_non_divisible_numbers(self):
        self.assertTrue(areEquivalent(5, 5))
        self.assertTrue(areEquivalent(7, 7))
        self.assertTrue(areEquivalent(11, 11))

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            areEquivalent(1.5, 2)

    def test_negative_numbers(self):
        self.assertTrue(areEquivalent(-1, -1))
        self.assertTrue(areEquivalent(-2, -2))
        self.assertTrue(areEquivalent(-3, -3))
