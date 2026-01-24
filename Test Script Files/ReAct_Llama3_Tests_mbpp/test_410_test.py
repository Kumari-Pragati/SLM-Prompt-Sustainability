import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)

    def test_edge_case_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_edge_case_single_element_list(self):
        self.assertEqual(min_val([5]), 5)

    def test_edge_case_list_with_non_integers(self):
        self.assertIsNone(min_val([1, 2, 'a', 4, 5]))

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(min_val([-5, -3, -1]), -5)

    def test_edge_case_list_with_positive_numbers(self):
        self.assertEqual(min_val([5, 3, 1]), 1)

    def test_edge_case_list_with_mixed_sign_numbers(self):
        self.assertEqual(min_val([-5, 3, -1]), -5)
