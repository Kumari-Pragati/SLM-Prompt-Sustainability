import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_empty_list(self):
        """Tests that an empty list returns -1"""
        self.assertEqual(first_odd([]), -1)

    def test_all_even(self):
        """Tests that a list of all even numbers returns -1"""
        self.assertEqual(first_odd([2, 4, 6]), -1)

    def test_single_odd(self):
        """Tests that a list containing a single odd number returns that number"""
        self.assertEqual(first_odd([1]), 1)

    def test_single_even(self):
        """Tests that a list containing a single even number returns -1"""
        self.assertEqual(first_odd([2]), -1)

    def test_mixed_odd_even(self):
        """Tests that a list containing a mix of odd and even numbers returns the first odd number"""
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)

    def test_negative_numbers(self):
        """Tests that the function works with negative numbers"""
        self.assertEqual(first_odd([-1, -3, -5]), -1)
        self.assertEqual(first_odd([-1, 1, -3, 5]), 1)

    def test_floats(self):
        """Tests that the function works with floats"""
        self.assertEqual(first_odd([1.5, 2.0, 3.5]), 1.5)

    def test_raises_ValueError(self):
        """Tests that the function raises a ValueError when given an empty iterable"""
        with self.assertRaises(ValueError):
            first_odd(())
