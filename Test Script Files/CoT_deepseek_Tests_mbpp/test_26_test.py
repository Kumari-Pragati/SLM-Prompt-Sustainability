import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_typical_case(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 3
        self.assertTrue(check_k_elements(test_list, K))

    def test_typical_case_with_duplicates(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (9, 9, 9)]
        K = 9
        self.assertTrue(check_k_elements(test_list, K))

    def test_typical_case_with_different_types(self):
        test_list = [(1, '2', 3), (4, 5, 6), (7, 8, 9)]
        K = 3
        self.assertFalse(check_k_elements(test_list, K))

    def test_empty_list(self):
        test_list = []
        K = 3
        self.assertTrue(check_k_elements(test_list, K))

    def test_list_with_single_tuple(self):
        test_list = [(1, 2, 3)]
        K = 4
        self.assertFalse(check_k_elements(test_list, K))

    def test_list_with_single_element(self):
        test_list = [3]
        K = 3
        self.assertTrue(check_k_elements(test_list, K))

    def test_invalid_input_type(self):
        test_list = [(1, 2, 3), '4', 5]
        K = 3
        with self.assertRaises(TypeError):
            check_k_elements(test_list, K)
