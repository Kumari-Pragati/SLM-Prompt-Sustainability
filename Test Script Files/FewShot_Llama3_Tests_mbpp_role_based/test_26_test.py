import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):
    def test_single_element_list(self):
        self.assertTrue(check_k_elements([(1,)], 1))

    def test_multiple_elements_list(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6)], 3))

    def test_list_with_non_k_elements(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 7))

    def test_list_with_k_elements(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (3, 3, 3)], 3))

    def test_empty_list(self):
        self.assertTrue(check_k_elements([], 1))

    def test_list_with_empty_tuple(self):
        self.assertTrue(check_k_elements([(), (1, 2)], 1))

    def test_list_with_k_elements_and_empty_tuple(self):
        self.assertTrue(check_k_elements([(), (1, 2), (1, 2, 3)], 1))
