import unittest
from468_code import max_product

class TestMaxProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), 120)
        self.assertEqual(max_product([0, 0, 0, 0, 0], 5), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_product([1], 1), 1)

    def test_edge_case_empty_list(self):
        with self.assertRaises(ValueError):
            max_product([], 1)

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            max_product([1], -1)

    def test_corner_case_decreasing_sequence(self):
        self.assertEqual(max_product([5, 4, 3, 2, 1], 5), 120)

    def test_corner_case_increasing_sequence(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 120)
