import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(unique_product([1, 2, 3, 4]), 24)

    def test_edge_case_single_element(self):
        self.assertEqual(unique_product([5]), 5)

    def test_boundary_case_empty_list(self):
        self.assertEqual(unique_product([]), 1)

    def test_boundary_case_all_same_elements(self):
        self.assertEqual(unique_product([2, 2, 2, 2]), 16)

    def test_error_handling_duplicate_elements(self):
        with self.assertRaises(TypeError):
            unique_product([1, 2, 2])
