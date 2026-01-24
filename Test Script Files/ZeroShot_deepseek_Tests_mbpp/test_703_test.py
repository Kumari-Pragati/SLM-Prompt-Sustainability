import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_key_present(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertTrue(is_key_present(d, 'b'))

    def test_key_absent(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertFalse(is_key_present(d, 'd'))

    def test_empty_dict(self):
        d = {}
        self.assertFalse(is_key_present(d, 'a'))

    def test_key_present_multiple_times(self):
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
        self.assertTrue(is_key_present(d, 1))
