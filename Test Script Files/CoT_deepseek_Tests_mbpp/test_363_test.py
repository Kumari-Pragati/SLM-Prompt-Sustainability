import unittest
from mbpp_363_code import add_K_element

class TestAddKElements(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = 2
        expected_output = [(3, 4, 5), (6, 7, 8)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_single_element(self):
        test_list = [[1]]
        K = 2
        expected_output = [(3,)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_empty_list(self):
        test_list = [[]]
        K = 2
        expected_output = [()]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_negative_K(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = -2
        expected_output = [(0, 1, 2), (2, 3, 4)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_non_integer_elements(self):
        test_list = [['1', '2', '3'], ['4', '5', '6']]
        K = 2
        expected_output = [('3', '4', '5'), ('6', '7', '8')]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = 'not a list'
        K = 2
        with self.assertRaises(TypeError):
            add_K_element(test_list, K)
