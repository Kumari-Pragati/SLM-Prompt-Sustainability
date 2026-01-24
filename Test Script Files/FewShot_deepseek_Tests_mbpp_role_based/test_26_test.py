import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 3
        self.assertTrue(check_k_elements(test_list, K))

    def test_edge_condition(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 10
        self.assertFalse(check_k_elements(test_list, K))

    def test_boundary_condition(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 9
        self.assertTrue(check_k_elements(test_list, K))

    def test_invalid_input(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 'K'
        with self.assertRaises(TypeError):
            check_k_elements(test_list, K)
