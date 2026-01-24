import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):

    def test_typical_input(self):
        test_list = [[1, 2], [2, 1], [3, 3], [4, 4], [5, 5]]
        expected_output = {(1, 2): 1, (2, 1): 1, (3, 3): 1, (4, 4): 1, (5, 5): 1}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_edge_case_empty_list(self):
        test_list = []
        expected_output = {}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_edge_case_single_element_list(self):
        test_list = [[1, 2]]
        expected_output = {(1, 2): 1}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_edge_case_single_element_list_with_duplicates(self):
        test_list = [[1, 2], [1, 2]]
        expected_output = {(1, 2): 2}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_edge_case_duplicates(self):
        test_list = [[1, 2], [2, 1], [1, 2]]
        expected_output = {(1, 2): 2, (2, 1): 1}
        self.assertEqual(check_occurences(test_list), expected_output)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            check_occurences("invalid input")

    def test_invalid_input_non_list_with_duplicates(self):
        with self.assertRaises(TypeError):
            check_occurences([1, 2, 3], "invalid input")
