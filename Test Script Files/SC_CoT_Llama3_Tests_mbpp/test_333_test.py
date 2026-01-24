import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_typical_input(self):
        input_list = [[1, 5], [2, 3], [3, 1]]
        expected_output = [[1, 5], [2, 3], [3, 1]]
        self.assertEqual(Sort(input_list), expected_output)

    def test_edge_case(self):
        input_list = [[1, 5], [2, 5], [3, 1]]
        expected_output = [[1, 5], [2, 5], [3, 1]]
        self.assertEqual(Sort(input_list), expected_output)

    def test_edge_case_reverse(self):
        input_list = [[3, 1], [2, 5], [1, 5]]
        expected_output = [[3, 1], [2, 5], [1, 5]]
        self.assertEqual(Sort(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(Sort(input_list), expected_output)

    def test_single_element_list(self):
        input_list = [[1, 5]]
        expected_output = [[1, 5]]
        self.assertEqual(Sort(input_list), expected_output)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            Sort("Invalid input")
