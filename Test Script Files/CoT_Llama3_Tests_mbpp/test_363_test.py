import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):

    def test_typical_input(self):
        test_list = [(1, 2), (3, 4)]
        K = 5
        expected_output = [(6, 7), (8, 9)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_edge_case_empty_list(self):
        test_list = []
        K = 5
        expected_output = []
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_edge_case_single_element_list(self):
        test_list = [(1, 2)]
        K = 5
        expected_output = [(6, 7)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_edge_case_K_zero(self):
        test_list = [(1, 2)]
        K = 0
        expected_output = [(1, 2)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_invalid_input_non_integer_K(self):
        test_list = [(1, 2)]
        K = 'five'
        with self.assertRaises(TypeError):
            add_K_element(test_list, K)

    def test_invalid_input_non_list_input(self):
        test_list = 'not a list'
        K = 5
        with self.assertRaises(TypeError):
            add_K_element(test_list, K)
