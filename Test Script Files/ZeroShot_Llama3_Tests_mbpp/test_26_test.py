import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_check_k_elements_true(self):
        self.assertTrue(check_k_elements([(1, 1, 1), (1, 1, 1)], 1))

    def test_check_k_elements_false(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (1, 2, 3)], 1))

    def test_check_k_elements_empty_list(self):
        self.assertTrue(check_k_elements([], 1))

    def test_check_k_elements_single_element(self):
        self.assertTrue(check_k_elements([(1,)], 1))

    def test_check_k_elements_single_element_false(self):
        self.assertFalse(check_k_elements([(1,)], 2))

    def test_check_k_elements_multiple_elements(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (1, 2, 3)], 2))

    def test_check_k_elements_multiple_elements_true(self):
        self.assertTrue(check_k_elements([(1, 1, 1), (1, 1, 1)], 1))
