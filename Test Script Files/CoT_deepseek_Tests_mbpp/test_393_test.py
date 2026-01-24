import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_typical_case(self):
        input_list = [['a', 'bb', 'ccc'], ['dddd', 'ee'], ['fff']]
        expected_output = (4, ['dddd', 'ee'])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = (0, [])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_single_element_list(self):
        input_list = [['a']]
        expected_output = (1, ['a'])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_all_same_length_lists(self):
        input_list = [['a', 'b'], ['c', 'd'], ['e', 'f']]
        expected_output = (2, ['e', 'f'])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_empty_strings(self):
        input_list = [[''], ['a', 'b'], ['c', 'd', 'e']]
        expected_output = (0, [''])
        self.assertEqual(max_length_list(input_list), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_length_list(123)
