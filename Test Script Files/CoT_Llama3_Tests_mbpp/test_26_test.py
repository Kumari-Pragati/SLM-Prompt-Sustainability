import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3))

    def test_edge_case_all_elements_match(self):
        self.assertTrue(check_k_elements([(1, 1, 1), (2, 2, 2), (3, 3, 3)], 1))

    def test_edge_case_no_elements_match(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 10))

    def test_edge_case_empty_list(self):
        self.assertTrue(check_k_elements([], 1))

    def test_edge_case_single_element_list(self):
        self.assertTrue(check_k_elements([(1,)], 1))

    def test_edge_case_single_element_list_no_match(self):
        self.assertFalse(check_k_elements([(1,)], 2))

    def test_edge_case_single_element_list_match(self):
        self.assertTrue(check_k_elements([(1,)], 1))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            check_k_elements(123, 1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 'a')
