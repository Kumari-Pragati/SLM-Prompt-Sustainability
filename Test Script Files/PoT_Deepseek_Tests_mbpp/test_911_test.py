import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_product([1, 2, 3, 4]), 24)

    def test_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4]), -6)

    def test_with_zero(self):
        self.assertEqual(maximum_product([-1, -2, -3, 0]), 0)

    def test_with_one(self):
        self.assertEqual(maximum_product([1, 2, 3, 4]), 24)

    def test_with_two_same_numbers(self):
        self.assertEqual(maximum_product([1, 1, 1, 1]), 1)

    def test_with_three_same_numbers(self):
        self.assertEqual(maximum_product([1, 1, 1, 1]), 1)

    def test_with_two_pairs_of_same_numbers(self):
        self.assertEqual(maximum_product([1, 1, 2, 2]), 4)

    def test_with_three_pairs_of_same_numbers(self):
        self.assertEqual(maximum_product([1, 1, 1, 2, 2, 2]), 4)

    def test_with_all_same_numbers(self):
        self.assertEqual(maximum_product([1, 1, 1, 1, 1, 1]), 1)

    def test_with_large_numbers(self):
        self.assertEqual(maximum_product([100, 200, 300, 400]), 24000000)

    def test_with_small_numbers(self):
        self.assertEqual(maximum_product([-10, -20, -30, -40]), -2400)

    def test_with_mixed_numbers(self):
        self.assertEqual(maximum_product([-1, -2, 3, 4]), 24)

    def test_with_empty_list(self):
        with self.assertRaises(ValueError):
            maximum_product([])

    def test_with_single_element(self):
        with self.assertRaises(ValueError):
            maximum_product([1])

    def test_with_two_elements(self):
        with self.assertRaises(ValueError):
            maximum_product([1, 2])
