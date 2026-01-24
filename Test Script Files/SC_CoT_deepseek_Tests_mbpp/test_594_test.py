import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(diff_even_odd([1, 2, 3, 4]), 2)

    def test_only_evens(self):
        self.assertEqual(diff_even_odd([2, 4, 6]), -1)

    def test_only_odds(self):
        self.assertEqual(diff_even_odd([1, 3, 5]), -1)

    def test_empty_list(self):
        self.assertEqual(diff_even_odd([]), -1)

    def test_all_negative_numbers(self):
        self.assertEqual(diff_even_odd([-1, -2, -3, -4]), 2)

    def test_mixed_negative_numbers(self):
        self.assertEqual(diff_even_odd([-1, 2, -3, 4]), 2)

    def test_large_numbers(self):
        self.assertEqual(diff_even_odd([1000, 2000, 3000, 4000]), 2000)

    def test_duplicate_numbers(self):
        self.assertEqual(diff_even_odd([2, 2, 3, 4]), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            diff_even_odd("not a list")
