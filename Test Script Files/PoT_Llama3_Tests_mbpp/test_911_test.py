import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 60)

    def test_edge_case_max_three(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6]), 60)

    def test_edge_case_min_two(self):
        self.assertEqual(maximum_product([-1, -2, 3, 4, 5, 6]), 60)

    def test_edge_case_max_three_min_two(self):
        self.assertEqual(maximum_product([-1, -2, 3, 4, 5, 6, 7]), 210)

    def test_edge_case_max_three_max_two(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6, 7]), 210)

    def test_edge_case_min_three(self):
        self.assertEqual(maximum_product([-1, -2, -3, 4, 5, 6]), 180)

    def test_edge_case_max_three_max_one(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6, 7, 8]), 1680)

    def test_edge_case_min_three_min_two(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5, -6]), 6)

    def test_edge_case_max_three_max_one_max_two(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2520)
