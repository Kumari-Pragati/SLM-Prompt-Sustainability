import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):
    def test_typical_input(self):
        input_dict = {'a': 1, 'b': None, 'c': 3, 'd': None, 'e': 5}
        expected_output = {'a': 1, 'c': 3, 'e': 5}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_edge_case_empty_input(self):
        input_dict = {}
        expected_output = {}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_edge_case_all_none_input(self):
        input_dict = {'a': None, 'b': None, 'c': None}
        expected_output = {}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_edge_case_all_non_none_input(self):
        input_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_output = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_edge_case_mixed_input(self):
        input_dict = {'a': 1, 'b': None, 'c': 3, 'd': None, 'e': 5}
        expected_output = {'a': 1, 'c': 3, 'e': 5}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_invalid_input_non_dict(self):
        with self.assertRaises(TypeError):
            drop_empty(123)
