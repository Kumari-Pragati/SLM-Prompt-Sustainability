import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):
    def test_typical_case(self):
        test_list = [(1, 2), (3, 4)]
        K = 5
        expected_result = [(6, 7), (8, 9)]
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_edge_case_empty_list(self):
        test_list = []
        K = 5
        expected_result = []
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_edge_case_single_element_list(self):
        test_list = [(1, 2)]
        K = 5
        expected_result = [(6, 7)]
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_edge_case_K_zero(self):
        test_list = [(1, 2)]
        K = 0
        expected_result = [(1, 2)]
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_edge_case_K_negative(self):
        test_list = [(1, 2)]
        K = -5
        expected_result = [(1 - 5, 2 - 5)]
        self.assertEqual(add_K_element(test_list, K), expected_result)
