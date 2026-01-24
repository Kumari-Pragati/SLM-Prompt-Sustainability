import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)
        self.assertEqual(maximum_product([-1, -2, -3]), 6)
        self.assertEqual(maximum_product([1, 2, -3]), 6)
        self.assertEqual(maximum_product([-1, 2, 3]), 6)

    def test_edge_case_single_element(self):
        self.assertEqual(maximum_product([1]), 1)
        self.assertEqual(maximum_product([-1]), 1)

    def test_edge_case_two_elements(self):
        self.assertEqual(maximum_product([1, 2]), 6)
        self.assertEqual(maximum_product([-1, -2]), 4)

    def test_edge_case_three_elements(self):
        self.assertEqual(maximum_product([1, 2, 3, 4]), 24)
        self.assertEqual(maximum_product([-1, -2, -3, -4]), 24)

    def test_corner_case_all_zero(self):
        self.assertEqual(maximum_product([0, 0, 0]), 0)

    def test_corner_case_all_negative(self):
        self.assertEqual(maximum_product([-5, -3, -2]), 30)

    def test_corner_case_all_positive(self):
        self.assertEqual(maximum_product([5, 3, 2]), 30)
