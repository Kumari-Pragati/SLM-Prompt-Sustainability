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
        test_dict = {'a': 1}
        expected_output = ['a']
        self.assertEqual(get_key(test_dict), expected_output)

    def test_duplicate_keys(self):
        test_dict = {'a': 1, 'b': 2, 'a': 3}
        expected_output = ['a', 'b']
        self.assertEqual(get_key(test_dict), expected_output)

    def test_non_dict_input(self):
        with self.assertRaises(TypeError):
            get_key('not a dict')
