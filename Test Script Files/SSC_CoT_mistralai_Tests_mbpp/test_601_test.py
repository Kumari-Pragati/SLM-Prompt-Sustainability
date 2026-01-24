import unittest
from mbpp_601_code import Iterable
from unittest.case import skipIf

from six import integer_types

class TestMaxChainLength(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(max_chain_length([Pair(1, 0), Pair(2, 1), Pair(3, 2)], 3), 3)
        self.assertEqual(max_chain_length([Pair(1, 0), Pair(2, 1), Pair(1, 2)], 3), 2)
        self.assertEqual(max_chain_length([Pair(1, 0), Pair(2, 1), Pair(0, 2)], 3), 1)

    def test_empty_input(self):
        self.assertEqual(max_chain_length([], 0), 0)

    def test_single_element_input(self):
        self.assertEqual(max_chain_length([Pair(1, 0)], 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_chain_length([Pair(-1, 0), Pair(-2, -1)], 2), 2)

    def test_zero_numbers(self):
        self.assertEqual(max_chain_length([Pair(0, 0)], 1), 1)
        self.assertEqual(max_chain_length([Pair(0, 0), Pair(0, 0)], 2), 1)

    def test_invalid_input(self):
        # Test if the function handles invalid inputs
        with self.assertRaises(TypeError):
            max_chain_length([1, 2], 'string')
        with self.assertRaises(TypeError):
            max_chain_length([1, 2], None)
        with self.assertRaises(TypeError):
            max_chain_length([1, 2], 3.5)
        with self.assertRaises(TypeError):
            max_chain_length([Pair(1, 2), Pair(3, 4)], 5.0)
        with self.assertRaises(ValueError):
            max_chain_length([Pair(1, 2)], -1)

    @skipIf(not all(isinstance(x, integer_types) for x in range(10)), "Skipping test on non-integer types")
    def test_large_input(self):
        # Test large input with integers only
        self.assertEqual(max_chain_length(list(map(Pair, zip(range(10), range(9, -1, -1)))), 10), 10)
