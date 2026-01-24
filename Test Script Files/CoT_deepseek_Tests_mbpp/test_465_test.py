import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_typical_case(self):
        input_dict = {'a': 1, 'b': None, 'c': 2, 'd': None}
        expected_output = {'a': 1, 'c': 2}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_empty_dict(self):
        input_dict = {}
        expected_output = {}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_all_none_values(self):
        input_dict = {'a': None, 'b': None, 'c': None}
        expected_output = {}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_no_none_values(self):
        input_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_output = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_mixed_values(self):
        input_dict = {'a': 1, 'b': None, 'c': 'string', 'd': 0}
        expected_output = {'a': 1, 'c': 'string', 'd': 0}
        self.assertEqual(drop_empty(input_dict), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            drop_empty(123)

        with self.assertRaises(TypeError):
            drop_empty('string')

        with self.assertRaises(TypeError):
            drop_empty(None)
