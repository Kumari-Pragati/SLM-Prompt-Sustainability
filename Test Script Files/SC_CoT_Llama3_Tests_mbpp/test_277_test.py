import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_typical_input(self):
        dict_input = {'a':1, 'b':2, 'c':3}
        expected_output = {'b':2, 'c':3}
        self.assertEqual(dict_filter(dict_input, 2), expected_output)

    def test_edge_case(self):
        dict_input = {'a':1, 'b':2, 'c':1.9}
        expected_output = {'b':2}
        self.assertEqual(dict_filter(dict_input, 2), expected_output)

    def test_edge_case2(self):
        dict_input = {'a':1, 'b':2, 'c':2.1}
        expected_output = {}
        self.assertEqual(dict_filter(dict_input, 2), expected_output)

    def test_edge_case3(self):
        dict_input = {'a':1, 'b':2, 'c':2.0}
        expected_output = {'b':2, 'c':2.0}
        self.assertEqual(dict_filter(dict_input, 2), expected_output)

    def test_empty_dict(self):
        dict_input = {}
        expected_output = {}
        self.assertEqual(dict_filter(dict_input, 2), expected_output)

    def test_no_matching_values(self):
        dict_input = {'a':1, 'b':2, 'c':0.9}
        expected_output = {}
        self.assertEqual(dict_filter(dict_input, 2), expected_output)

    def test_non_integer_value(self):
        dict_input = {'a':1, 'b':2, 'c':2.5}
        expected_output = {'b':2}
        self.assertEqual(dict_filter(dict_input, 2), expected_output)
