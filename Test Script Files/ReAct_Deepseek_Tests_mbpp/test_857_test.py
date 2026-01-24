import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):

    def test_typical_case(self):
        input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(listify_list(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(listify_list(input_list), expected_output)

    def test_single_element(self):
        input_list = [1]
        expected_output = [[1]]
        self.assertEqual(listify_list(input_list), expected_output)

    def test_nested_list(self):
        input_list = [[1, 2], [3, 4]]
        expected_output = [[1, 2], [3, 4]]
        self.assertEqual(listify_list(input_list), expected_output)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            listify_list(None)
