import unittest
from mbpp_221_code import first_even

class TestFirstEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_even([1, 2, 3, 4]), 2)

    def test_empty_list(self):
        self.assertEqual(first_even([]), -1)

    def test_all_odd(self):
        self.assertEqual(first_even([1, 3, 5]), -1)

    def test_negative_numbers(self):
        self.assertEqual(first_even([-1, -3, -5, -7]), -1)

    def test_large_numbers(self):
        self.assertEqual(first_even([1000000000, 2, 3]), 2)

    def test_mixed_numbers(self):
        self.assertEqual(first_even([1, 3, 5, 7, 9, 10]), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_even('1, 2, 3, 4')
