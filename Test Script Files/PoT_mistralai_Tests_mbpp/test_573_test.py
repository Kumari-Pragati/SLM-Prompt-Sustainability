import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(unique_product([1, 2, 3, 4]), 24)
        self.assertEqual(unique_product([5, 6, 7, 8]), 8064)
        self.assertEqual(unique_product([-1, 0, 1]), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(unique_product([1]), 1)

    def test_edge_case_all_negative(self):
        self.assertEqual(unique_product([-1, -2, -3]), 6)

    def test_edge_case_all_zero(self):
        self.assertEqual(unique_product([0, 0, 0]), 1)

    def test_corner_case_duplicates(self):
        self.assertEqual(unique_product([1, 1, 2, 3]), 6)
        self.assertEqual(unique_product([1, 2, 2, 3]), 6)
        self.assertEqual(unique_product([1, 2, 3, 3]), 6)
