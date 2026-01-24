import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_all_elements_are_k(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 9))

    def test_not_all_elements_are_k(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 8))

    def test_empty_list(self):
        self.assertTrue(check_k_elements([], 0))

    def test_single_tuple(self):
        self.assertTrue(check_k_elements([(1, 2, 3)], 3))
        self.assertFalse(check_k_elements([(1, 2, 3)], 4))

    def test_mixed_types(self):
        self.assertFalse(check_k_elements([(1, '2', 3.0), (4, 5, 6), (7, 8, 9)], 8))
