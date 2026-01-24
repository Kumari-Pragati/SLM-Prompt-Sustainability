import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum_product([1, 2, 3, 4]), 24)

    def test_single_negative_number(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4]), -6)

    def test_two_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2, 3, 4]), 8)

    def test_all_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4]), -6)

    def test_with_zero(self):
        self.assertEqual(maximum_product([-1, -2, 0, 4]), 0)

    def test_with_two_zeros(self):
        self.assertEqual(maximum_product([-1, -2, 0, 0]), 0)

    def test_with_three_zeros(self):
        self.assertEqual(maximum_product([0, 0, 0, 0]), 0)

    def test_with_one_number(self):
        self.assertEqual(maximum_product([1]), 1)

    def test_with_two_numbers(self):
        self.assertEqual(maximum_product([1, 2]), 2)

    def test_with_three_numbers(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)

    def test_with_duplicates(self):
        self.assertEqual(maximum_product([1, 2, 2]), 4)

    def test_with_large_numbers(self):
        self.assertEqual(maximum_product([10**6, 10**6, 10**6]), 10**18)

    def test_with_small_numbers(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)

    def test_with_large_and_small_numbers(self):
        self.assertEqual(maximum_product([10**6, -10**6, 1]), -1)

    def test_with_large_and_small_numbers_and_zero(self):
        self.assertEqual(maximum_product([10**6, -10**6, 0, 1]), 0)

    def test_with_large_and_small_numbers_and_duplicates(self):
        self.assertEqual(maximum_product([10**6, -10**6, 1, 1]), 1)

    def test_with_invalid_input(self):
        with self.assertRaises(TypeError):
            maximum_product('not a list')
