import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_typical_case(self):
        input_list = [["apple", "banana"], ["cherry", "date"], ["elderberry"]]
        expected_output = (3, ["elderberry"])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_edge_case_empty_list(self):
        input_list = []
        expected_output = (0, [])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_edge_case_single_element_list(self):
        input_list = [["apple"]]
        expected_output = (1, ["apple"])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_edge_case_single_element_list_with_empty_string(self):
        input_list = [["", "banana"]]
        expected_output = (1, [""])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_edge_case_list_with_all_empty_strings(self):
        input_list = [["", "", ""]]
        expected_output = (1, [""])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_length_list("not a list")
