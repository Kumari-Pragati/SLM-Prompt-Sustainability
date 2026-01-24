import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):

    def test_typical_case(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected_output = {'a': 1, 'b': 5, 'c': 4}
        self.assertEqual(add_dict(d1, d2), expected_output)

    def test_empty_dicts(self):
        d1 = {}
        d2 = {}
        expected_output = {}
        self.assertEqual(add_dict(d1, d2), expected_output)

    def test_one_empty_dict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {}
        expected_output = {'a': 1, 'b': 2}
        self.assertEqual(add_dict(d1, d2), expected_output)

    def test_same_keys_different_values(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'b': 4}
        expected_output = {'a': 4, 'b': 6}
        self.assertEqual(add_dict(d1, d2), expected_output)

    def test_non_integer_values(self):
        d1 = {'a': '1', 'b': '2'}
        d2 = {'a': '3', 'b': '4'}
        expected_output = {'a': '13', 'b': '24'}
        self.assertEqual(add_dict(d1, d2), expected_output)

    def test_non_string_keys(self):
        d1 = {1: 1, 2: 2}
        d2 = {1: 3, 2: 4}
        expected_output = {1: 4, 2: 6}
        self.assertEqual(add_dict(d1, d2), expected_output)
