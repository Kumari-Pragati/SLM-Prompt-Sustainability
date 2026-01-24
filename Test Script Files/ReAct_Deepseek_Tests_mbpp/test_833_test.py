import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):

    def test_typical_case(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_output = ['a', 'b', 'c']
        self.assertEqual(get_key(test_dict), expected_output)

    def test_empty_dict(self):
        test_dict = {}
        expected_output = []
        self.assertEqual(get_key(test_dict), expected_output)

    def test_single_key_dict(self):
        test_dict = {'single': 1}
        expected_output = ['single']
        self.assertEqual(get_key(test_dict), expected_output)

    def test_duplicate_values_dict(self):
        test_dict = {'a': 1, 'b': 1, 'c': 1}
        expected_output = ['a', 'b', 'c']
        self.assertEqual(get_key(test_dict), expected_output)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            get_key(None)
