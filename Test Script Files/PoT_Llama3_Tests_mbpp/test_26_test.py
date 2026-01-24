import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_k_elements([(1, 1, 1), (2, 2, 2), (3, 3, 3)], 3))

    def test_edge_case_K_in_list(self):
        self.assertFalse(check_k_elements([(1, 1, 3), (2, 2, 2), (3, 3, 3)], 3))

    def test_edge_case_K_not_in_list(self):
        self.assertTrue(check_k_elements([(1, 1, 2), (2, 2, 2), (3, 3, 3)], 2))

    def test_edge_case_empty_list(self):
        self.assertTrue(check_k_elements([], 1))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_k_elements([(1,)], 1))

    def test_edge_case_single_element_list_K_not_in(self):
        self.assertFalse(check_k_elements([(1,)], 2))

    def test_edge_case_single_element_list_K_in(self):
        self.assertFalse(check_k_elements([(1,)], 1))

    def test_edge_case_single_element_list_K_in_list(self):
        self.assertFalse(check_k_elements([(1,)], 1))

    def test_edge_case_single_element_list_K_not_in_list(self):
        self.assertTrue(check_k_elements([(1,)], 2))

    def test_edge_case_single_element_list_K_in_list(self):
        self.assertFalse(check_k_elements([(1,)], 1))

    def test_edge_case_single_element_list_K_not_in_list(self):
        self.assertTrue(check_k_elements([(1,)], 2))
