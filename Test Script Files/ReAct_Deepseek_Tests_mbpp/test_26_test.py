import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6)], 3))

    def test_typical_case_with_duplicates(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 3)], 3))

    def test_typical_case_with_different_tuples(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6)], 6))

    def test_typical_case_with_multiple_Ks(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 2))

    def test_empty_list(self):
        self.assertTrue(check_k_elements([], 0))

    def test_single_tuple(self):
        self.assertTrue(check_k_elements([(1, 2, 3)], 3))

    def test_single_tuple_with_duplicates(self):
        self.assertTrue(check_k_elements([(1, 2, 3)], 2))

    def test_single_tuple_with_different_Ks(self):
        self.assertFalse(check_k_elements([(1, 2, 3)], 4))

    def test_single_element_tuple(self):
        self.assertTrue(check_k_elements([(3,)], 3))

    def test_single_element_tuple_with_different_Ks(self):
        self.assertFalse(check_k_elements([(3,)], 4))

    def test_all_elements_are_K(self):
        self.assertTrue(check_k_elements([(3, 3, 3)], 3))

    def test_all_elements_are_not_K(self):
        self.assertFalse(check_k_elements([(1, 2, 3)], 4))
