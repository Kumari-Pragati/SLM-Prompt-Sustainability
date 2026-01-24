import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 60)

    def test_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(maximum_product([-1, -2, 3, 4, 5]), 60)

    def test_single_number(self):
        self.assertEqual(maximum_product([1]), 1)

    def test_two_numbers(self):
        self.assertEqual(maximum_product([1, 2]), 2)

    def test_three_numbers(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)

    def test_duplicate_numbers(self):
        self.assertEqual(maximum_product([1, 1, 1, 1]), 1)

    def test_large_numbers(self):
        self.assertEqual(maximum_product([100, 200, 300, 400, 500]), 300000000000000)

    def test_small_numbers(self):
        self.assertEqual(maximum_product([-100, -200, -300, -400, -500]), -600000000000000)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            maximum_product([])

    def test_single_negative_number(self):
        self.assertEqual(maximum_product([-1]), -1)

    def test_two_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2]), -2)

    def test_three_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2, -3]), -6)
