import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)
        self.assertEqual(maximum_product([10, 20, 30]), 600)
        self.assertEqual(maximum_product([100, 200, 300]), 600000)

    def test_mixed_numbers(self):
        self.assertEqual(maximum_product([1, -2, 3]), 6)
        self.assertEqual(maximum_product([10, -20, 30]), 600)
        self.assertEqual(maximum_product([100, -200, 300]), 600000)

    def test_single_number(self):
        self.assertEqual(maximum_product([1]), 1)
        self.assertEqual(maximum_product([-1]), 1)
        self.assertEqual(maximum_product([0]), 0)

    def test_empty_list(self):
        self.assertEqual(maximum_product([]), 0)

    def test_single_element(self):
        self.assertEqual(maximum_product([1]), 1)
        self.assertEqual(maximum_product([-1]), 1)

    def test_two_elements(self):
        self.assertEqual(maximum_product([1, 2]), 2)
        self.assertEqual(maximum_product([-1, -2]), 4)
