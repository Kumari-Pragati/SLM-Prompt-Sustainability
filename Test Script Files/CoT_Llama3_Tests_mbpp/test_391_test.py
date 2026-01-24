import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(convert_list_dictionary(['a', 'b', 'c'], ['x', 'y', 'z'], [1, 2, 3]),
                         [{'a': {'x': 1}}, {'b': {'y': 2}}, {'c': {'z': 3}}])

    def test_empty_input(self):
        self.assertEqual(convert_list_dictionary([], [], []), [])

    def test_single_element_input(self):
        self.assertEqual(convert_list_dictionary(['a'], ['x'], [1]),
                         [{'a': {'x': 1}}])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            convert_list_dictionary('a', 'b', 'c')

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            convert_list_dictionary(['a', 'b'], ['x', 'y', 'z', 'w'], [1, 2, 3])
