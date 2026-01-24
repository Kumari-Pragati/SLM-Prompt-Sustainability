import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (1, 4))
        self.assertEqual(max_product([-1, -2, -3, -4]), (-1, -4))
        self.assertEqual(max_product([0, 1, 2]), (0, 2))

    def test_edge_case_single_element(self):
        self.assertIsNone(max_product([1]))

    def test_edge_case_empty_list(self):
        self.assertIsNone(max_product([]))

    def test_corner_case_all_negative(self):
        self.assertEqual(max_product([-1, -2, -3]), (-1, -3))

    def test_corner_case_all_positive(self):
        self.assertEqual(max_product([1, 2, 3]), (1, 3))

    def test_corner_case_all_zero(self):
        self.assertEqual(max_product([0, 0, 0]), (0, 0))
