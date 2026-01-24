import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3))

    def test_edge_case(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 10))

    def test_single_element_list(self):
        self.assertTrue(check_k_elements([(1,)], 1))

    def test_empty_list(self):
        self.assertTrue(check_k_elements([], 1))

    def test_k_not_in_list(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 10))

    def test_k_in_all_elements(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 7))

    def test_k_in_first_element(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 1))

    def test_k_in_last_element(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 9))

    def test_k_in_middle_element(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 5))

    def test_k_not_in_list_invalid_input(self):
        with self.assertRaises(TypeError):
            check_k_elements("not a list", 1)
