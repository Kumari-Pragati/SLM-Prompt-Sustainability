import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 60)
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), 120)
        self.assertEqual(maximum_product([1, -1, 0, -2, 3]), 0)

    def test_edge_cases(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)
        self.assertEqual(maximum_product([1, 2]), 2)
        self.assertEqual(maximum_product([1]), 1)
        self.assertEqual(maximum_product([-1, -2, -3]), -6)
        self.assertEqual(maximum_product([-1, -2]), -2)
        self.assertEqual(maximum_product([-1]), 1)

    def test_empty_list(self):
        self.assertEqual(maximum_product([]), 0)

    def test_single_negative_number(self):
        self.assertEqual(maximum_product([-1]), 1)

    def test_single_positive_number(self):
        self.assertEqual(maximum_product([1]), 1)

    def test_single_zero(self):
        self.assertEqual(maximum_product([0]), 0)

    def test_all_zeros(self):
        self.assertEqual(maximum_product([0, 0, 0]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2, -3]), -6)

    def test_all_positive_numbers(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)

    def test_all_negative_and_zero(self):
        self.assertEqual(maximum_product([0, -1, -2]), -2)

    def test_all_positive_and_zero(self):
        self.assertEqual(maximum_product([0, 1, 2]), 0)
