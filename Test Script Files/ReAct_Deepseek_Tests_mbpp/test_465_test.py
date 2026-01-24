import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_typical_case(self):
        input_dict = {'a': 1, 'b': None, 'c': 2}
        expected_dict = {'a': 1, 'c': 2}
        self.assertEqual(drop_empty(input_dict), expected_dict)

    def test_empty_dict(self):
        input_dict = {}
        expected_dict = {}
        self.assertEqual(drop_empty(input_dict), expected_dict)

    def test_all_empty_values(self):
        input_dict = {'a': None, 'b': None, 'c': None}
        expected_dict = {}
        self.assertEqual(drop_empty(input_dict), expected_dict)

    def test_all_non_empty_values(self):
        input_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(drop_empty(input_dict), expected_dict)

    def test_mixed_values(self):
        input_dict = {'a': 1, 'b': None, 'c': 0}
        expected_dict = {'a': 1, 'c': 0}
        self.assertEqual(drop_empty(input_dict), expected_dict)
