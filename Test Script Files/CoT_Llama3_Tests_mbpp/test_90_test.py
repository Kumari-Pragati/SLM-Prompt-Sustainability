import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(len_log([[1,2,3], [4,5,6], [7,8,9]]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(len_log([]), None)

    def test_edge_case_single_element_list(self):
        self.assertEqual(len_log([[1,2,3]]), 3)

    def test_edge_case_single_element_list_with_single_element(self):
        self.assertEqual(len_log([[1]]), 1)

    def test_edge_case_single_element_list_with_single_element_and_empty(self):
        self.assertEqual(len_log([[1], []]), 1)

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(len_log([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]), 3)

    def test_edge_case_multiple_elements_list_with_empty(self):
        self.assertEqual(len_log([[1,2,3], [4,5,6], [7,8,9], []]), 3)

    def test_edge_case_multiple_elements_list_with_empty_and_single_element(self):
        self.assertEqual(len_log([[1,2,3], [4,5,6], [7,8,9], [10]]), 3)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            len_log("Invalid input")

    def test_invalid_input_non_list_with_non_list(self):
        with self.assertRaises(TypeError):
            len_log([1, 2, 3], "Invalid input")
