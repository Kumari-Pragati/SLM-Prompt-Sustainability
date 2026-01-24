import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):
    def test_valid_list_of_integers(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)

    def test_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_list_with_non_integer_values(self):
        self.assertIsNone(min_val([1, 'a', 3]))

    def test_list_with_only_floats(self):
        self.assertIsNone(min_val([1.1, 2.2, 3.3]))

    def test_list_with_only_fractions(self):
        from fractions import Fraction
        self.assertIsNone(min_val([Fraction(1, 2), Fraction(3, 4), Fraction(5, 6)]))
