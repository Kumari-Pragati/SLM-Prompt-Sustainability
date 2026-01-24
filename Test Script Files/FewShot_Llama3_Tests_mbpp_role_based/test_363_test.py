import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):
    def test_add_k_element_with_positive_numbers(self):
        test_list = [(1, 2), (3, 4)]
        K = 5
        expected_result = [(6, 7), (8, 9)]
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_add_k_element_with_negative_numbers(self):
        test_list = [(-1, -2), (-3, -4)]
        K = 5
        expected_result = [(4, 3), (2, 1)]
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_add_k_element_with_zero(self):
        test_list = [(0, 0), (0, 1)]
        K = 2
        expected_result = [(2, 2), (2, 3)]
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_add_k_element_with_empty_list(self):
        test_list = []
        K = 5
        expected_result = []
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_add_k_element_with_non_integer_K(self):
        test_list = [(1, 2), (3, 4)]
        K = 5.5
        with self.assertRaises(TypeError):
            add_K_element(test_list, K)
