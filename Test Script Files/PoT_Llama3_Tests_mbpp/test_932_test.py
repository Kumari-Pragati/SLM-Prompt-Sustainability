import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_duplic_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_edge_case_duplicates(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates_order_matters(self):
        self.assertEqual(remove_duplic_list([4, 2, 3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates_order_matters_reverse(self):
        self.assertEqual(remove_duplic_list([5, 2, 4, 1, 3, 2, 4]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates_order_matters_reverse_empty(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_edge_case_duplicates_order_matters_reverse_single(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_edge_case_duplicates_order_matters_reverse_duplicates(self):
        self.assertEqual(remove_duplic_list([4, 2, 3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates_order_matters_reverse_duplicates_empty(self):
        self.assertEqual(remove_duplic_list([]), [])

    def test_edge_case_duplicates_order_matters_reverse_duplicates_single(self):
        self.assertEqual(remove_duplic_list([1]), [1])

    def test_edge_case_duplicates_order_matters_reverse_duplicates_duplicates(self):
        self.assertEqual(remove_duplic_list([4, 2, 3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])
