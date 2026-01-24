import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_typical_case(self):
        dict_input = {'a':1, 'b':2, 'c':3, 'd':4}
        expected_output = {'a':1, 'c':3, 'd':4}
        self.assertEqual(dict_filter(dict_input, 2), expected_output)

    def test_edge_case(self):
        dict_input = {'a':1, 'b':2, 'c':3, 'd':4}
        expected_output = {'a':1, 'b':2, 'c':3, 'd':4}
        self.assertEqual(dict_filter(dict_input, 1), expected_output)

    def test_edge_case2(self):
        dict_input = {'a':1, 'b':2, 'c':3, 'd':4}
        expected_output = {}
        self.assertEqual(dict_filter(dict_input, 5), expected_output)

    def test_error_case(self):
        dict_input = None
        with self.assertRaises(TypeError):
            dict_filter(dict_input, 1)

    def test_empty_dict(self):
        dict_input = {}
        expected_output = {}
        self.assertEqual(dict_filter(dict_input, 1), expected_output)

    def test_single_key_value(self):
        dict_input = {'a':1}
        expected_output = {'a':1}
        self.assertEqual(dict_filter(dict_input, 1), expected_output)
