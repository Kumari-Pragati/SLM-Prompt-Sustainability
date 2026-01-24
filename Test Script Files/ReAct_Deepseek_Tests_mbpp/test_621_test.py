import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_typical_case(self):
        test_list = ['1', '2', '3']
        K = 2
        expected_output = ['3', '4', '5']
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_edge_case_with_non_numeric_elements(self):
        test_list = ['1', 'a', '3']
        K = 1
        expected_output = ['2', 'a', '4']
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_edge_case_with_empty_list(self):
        test_list = []
        K = 1
        expected_output = []
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_edge_case_with_all_numeric_elements(self):
        test_list = ['9', '99', '999']
        K = 1
        expected_output = ['10', '100', '1000']
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_edge_case_with_large_numeric_elements(self):
        test_list = ['999999999', '9999999999']
        K = 1
        expected_output = ['1000000000', '10000000000']
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_error_case_with_non_string_elements(self):
        test_list = [1, '2', '3']
        K = 1
        with self.assertRaises(TypeError):
            increment_numerics(test_list, K)
