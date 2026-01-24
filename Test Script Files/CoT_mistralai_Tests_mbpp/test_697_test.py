import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_even([]), 0)

    def test_all_even(self):
        self.assertEqual(count_even([0, 2, 4, 6]), 4)

    def test_all_odd(self):
        self.assertEqual(count_even([1, 3, 5, 7]), 0)

    def test_mixed_even_odd(self):
        self.assertEqual(count_even([0, 1, 2, 3, 4, 5]), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_even([-2, -4, -6]), 3)

    def test_single_number(self):
        self.assertEqual(count_even([4]), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_even, "not a number")
