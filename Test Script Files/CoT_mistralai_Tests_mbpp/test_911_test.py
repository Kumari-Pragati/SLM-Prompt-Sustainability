import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 60)
        self.assertEqual(maximum_product([10, 20, 30, 40, 50]), 12000)
        self.assertEqual(maximum_product([100, 200, 300, 400, 500]), 1200000)

    def test_negative_numbers(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), 60)
        self.assertEqual(maximum_product([-10, -20, -30, -40, -50]), 12000)
        self.assertEqual(maximum_product([-100, -200, -300, -400, -500]), 1200000)

    def test_mixed_numbers(self):
        self.assertEqual(maximum_product([1, -2, 3, -4, 5]), 60)
        self.assertEqual(maximum_product([-1, 2, -3, 4, -5]), 60)
        self.assertEqual(maximum_product([10, -20, 30, -40, 50]), 12000)
        self.assertEqual(maximum_product([-10, 20, -30, 40, -50]), 12000)

    def test_single_number(self):
        self.assertEqual(maximum_product([1]), 1)
        self.assertEqual(maximum_product([-1]), 1)
        self.assertEqual(maximum_product([0]), 0)

    def test_empty_list(self):
        self.assertEqual(maximum_product([]), 0)

    def test_single_negative_number(self):
        self.assertEqual(maximum_product([-1]), 1)
