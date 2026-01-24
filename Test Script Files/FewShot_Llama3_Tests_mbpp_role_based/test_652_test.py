import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = "[[1, 4, 7], [2, 5, 8], [3, 6, 9]]"
        self.assertEqual(matrix_to_list(test_list), expected_output)

    def test_empty_list(self):
        test_list = []
        expected_output = "[]"
        self.assertEqual(matrix_to_list(test_list), expected_output)

    def test_single_element_list(self):
        test_list = [[1, 2, 3]]
        expected_output = "[[1, 2, 3]]"
        self.assertEqual(matrix_to_list(test_list), expected_output)

    def test_list_with_single_element_sublists(self):
        test_list = [[1], [2], [3]]
        expected_output = "[[1], [2], [3]]"
        self.assertEqual(matrix_to_list(test_list), expected_output)

    def test_list_with_empty_sublists(self):
        test_list = [[1, 2, 3], [], [4, 5, 6]]
        expected_output = "[[1, 2, 3], [], [4, 5, 6]]"
        self.assertEqual(matrix_to_list(test_list), expected_output)
