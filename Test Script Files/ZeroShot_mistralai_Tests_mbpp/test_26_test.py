import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(check_k_elements([], 1))

    def test_single_element_list(self):
        self.assertTrue(check_k_elements([[1]], 1))
        self.assertFalse(check_k_elements([[1]], 2))

    def test_multiple_elements_list(self):
        self.assertTrue(check_k_elements([[1], [1]], 1))
        self.assertFalse(check_k_elements([[1], [2]], 1))
        self.assertTrue(check_k_elements([[1], [2]], 2))

    def test_mixed_elements_list(self):
        self.assertFalse(check_k_elements([[1, 2], [1, 3]], 2))
        self.assertTrue(check_k_elements([[1, 2], [1, 2]], 2))
