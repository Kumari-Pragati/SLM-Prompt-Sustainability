import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_typical_case(self):
        input_list = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h', 'i']]
        expected_output = (2, ['d', 'e'])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = (0, [])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_single_element_list(self):
        input_list = [['a', 'b', 'c']]
        expected_output = (3, ['a', 'b', 'c'])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_all_same_length_lists(self):
        input_list = [['a', 'b'], ['c', 'd'], ['e', 'f']]
        expected_output = (2, ['a', 'b'])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_empty_strings(self):
        input_list = [[''], ['b', 'c'], ['d', 'e', 'f']]
        expected_output = (0, [''])
        self.assertEqual(min_length_list(input_list), expected_output)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            min_length_list(None)
