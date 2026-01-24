import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(check_k_elements([(1, 1, 1), (2, 2, 2)], 2))

    def test_empty_input(self):
        self.assertFalse(check_k_elements([], 2))

    def test_single_element_input(self):
        self.assertFalse(check_k_elements([(1,)], 2))

    def test_k_not_in_list(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 7))

    def test_k_in_all_elements(self):
        self.assertTrue(check_k_elements([(1, 1, 1), (2, 2, 2)], 1))

    def test_k_in_some_elements(self):
        self.assertFalse(check_k_elements([(1, 1, 2), (3, 4, 2)], 2))
