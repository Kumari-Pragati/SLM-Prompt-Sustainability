import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):

    def test_typical_case(self):
        test_list = ['1', '2', '3']
        K = 2
        expected_output = ['3', '4', '5']
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_with_non_numeric_elements(self):
        test_list = ['1', 'a', '3']
        K = 2
        expected_output = ['3', 'a', '5']
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_with_negative_K(self):
        test_list = ['1', '2', '3']
        K = -1
        expected_output = ['0', '1', '2']
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_with_large_K(self):
        test_list = ['9', '99', '999']
        K = 100
        expected_output = ['109', '1099', '10999']
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_with_empty_list(self):
        test_list = []
        K = 2
        expected_output = []
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_with_all_numeric_elements(self):
        test_list = ['10', '20', '30']
        K = 5
        expected_output = ['15', '25', '35']
        self.assertEqual(increment_numerics(test_list, K), expected_output)

    def test_with_leading_zeroes(self):
        test_list = ['01', '02', '03']
        K = 1
        expected_output = ['02', '03', '04']
        self.assertEqual(increment_numerics(test_list, K), expected_output)
