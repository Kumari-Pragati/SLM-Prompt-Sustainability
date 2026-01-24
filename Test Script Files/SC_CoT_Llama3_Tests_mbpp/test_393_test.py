import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):
    def test_typical_input(self):
        input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_max_length = 3
        expected_max_list = [1, 2, 3]
        self.assertEqual(max_length_list(input_list), (expected_max_length, expected_max_list))

    def test_edge_case_empty_list(self):
        input_list = []
        expected_max_length = 0
        expected_max_list = []
        self.assertEqual(max_length_list(input_list), (expected_max_length, expected_max_list))

    def test_edge_case_single_element_list(self):
        input_list = [['a']]
        expected_max_length = 1
        expected_max_list = ['a']
        self.assertEqual(max_length_list(input_list), (expected_max_length, expected_max_list))

    def test_edge_case_list_with_duplicates(self):
        input_list = [[1, 2, 3], [1, 2, 3], [4, 5, 6]]
        expected_max_length = 3
        expected_max_list = [1, 2, 3]
        self.assertEqual(max_length_list(input_list), (expected_max_length, expected_max_list))

    def test_edge_case_list_with_empty_strings(self):
        input_list = [['', 'a', 'b'], ['c', 'd', 'e']]
        expected_max_length = 3
        expected_max_list = ['c', 'd', 'e']
        self.assertEqual(max_length_list(input_list), (expected_max_length, expected_max_list))

    def test_edge_case_list_with_mixed_types(self):
        input_list = [['a', 1, 2.0], ['b', 3, 4.0]]
        expected_max_length = 3
        expected_max_list = ['a', 1, 2.0]
        self.assertEqual(max_length_list(input_list), (expected_max_length, expected_max_list))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_length_list('not a list')
