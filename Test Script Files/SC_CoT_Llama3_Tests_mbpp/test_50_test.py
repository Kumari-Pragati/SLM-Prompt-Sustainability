import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_typical_input(self):
        input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = (3, [1, 2, 3])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_edge_case_empty_list(self):
        input_list = []
        expected_output = (0, [])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_edge_case_single_element_list(self):
        input_list = [[1, 2, 3]]
        expected_output = (3, [1, 2, 3])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_edge_case_all_equal_length(self):
        input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = (3, [1, 2, 3])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_edge_case_all_zero_length(self):
        input_list = [[], [], []]
        expected_output = (0, [])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            min_length_list("Invalid input")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            min_length_list(123)
