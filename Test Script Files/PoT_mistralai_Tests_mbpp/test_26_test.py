import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, K)], K))
        self.assertTrue(check_k_elements([(K, K, K), (K, K, K)], K))

    def test_edge_case_empty_list(self):
        self.assertFalse(check_k_elements([], K))

    def test_edge_case_empty_tuple(self):
        self.assertFalse(check_k_elements([(K,), (K,)], K))

    def test_edge_case_single_tuple(self):
        self.assertFalse(check_k_elements([(K,)], K))

    def test_edge_case_single_element(self):
        self.assertFalse(check_k_elements([K], K))

    def test_corner_case_different_k(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 2)], K))
