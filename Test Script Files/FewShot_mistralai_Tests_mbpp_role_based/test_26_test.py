import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):
    def test_k_in_list(self):
        self.assertTrue(check_k_elements([(1, 2, 3, 4), 3], 3))
        self.assertTrue(check_k_elements([(1, 2, 3, 4), 4], 4))

    def test_k_not_in_list(self):
        self.assertFalse(check_k_elements([(1, 2, 3, 4), 5], 5))

    def test_empty_list(self):
        self.assertFalse(check_k_elements([], 1))

    def test_single_element_list(self):
        self.assertTrue(check_k_elements([(1,)], 1))

    def test_k_in_single_element_list(self):
        self.assertFalse(check_k_elements([(1,)], 2))

    def test_k_not_in_single_element_list(self):
        self.assertTrue(check_k_elements([(1,)], 1))
