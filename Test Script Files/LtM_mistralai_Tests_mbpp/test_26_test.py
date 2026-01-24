import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(check_k_elements([(1, 1), (2, 2), (3, 3)], 1))
        self.assertTrue(check_k_elements([(1, 1), (2, 2), (3, 3)], 2))
        self.assertTrue(check_k_elements([(1, 1), (2, 2), (3, 3)], 3))

    def test_edge_case_empty_list(self):
        self.assertTrue(check_k_elements([], 1))

    def test_edge_case_single_tuple(self):
        self.assertTrue(check_k_elements([(1,)], 1))
        self.assertFalse(check_k_elements([(1,)], 2))

    def test_edge_case_single_element(self):
        self.assertTrue(check_k_elements([1], 1))
        self.assertFalse(check_k_elements([2], 1))

    def test_edge_case_k_not_in_list(self):
        self.assertFalse(check_k_elements([(1, 1), (2, 2), (3, 3)], 4))

    def test_complex_case_mixed_elements(self):
        self.assertFalse(check_k_elements([(1, 1), (2, 2), (3, 3), (4, 1)], 1))
