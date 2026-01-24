import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_key_present(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertTrue(is_key_present(dictionary, 'b'))

    def test_key_absent(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertFalse(is_key_present(dictionary, 'd'))

    def test_key_present_with_case_insensitivity(self):
        dictionary = {'A': 1, 'B': 2, 'C': 3}
        self.assertTrue(is_key_present(dictionary, 'b'))

    def test_key_absent_with_case_insensitivity(self):
        dictionary = {'A': 1, 'B': 2, 'C': 3}
        self.assertFalse(is_key_present(dictionary, 'd'))

    def test_empty_dictionary(self):
        dictionary = {}
        self.assertFalse(is_key_present(dictionary, 'a'))

    def test_empty_input(self):
        dictionary = None
        with self.assertRaises(TypeError):
            is_key_present(dictionary, 'a')

    def test_non_dict_input(self):
        dictionary ='string'
        with self.assertRaises(TypeError):
            is_key_present(dictionary, 'a')
