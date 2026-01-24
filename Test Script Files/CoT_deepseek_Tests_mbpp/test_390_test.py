import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_string(['Hello', 'World'], 'Hello, {}.'), ['Hello, Hello.', 'Hello, World.'])

    def test_empty_list(self):
        self.assertEqual(add_string([], 'Hello, {}.'), [])

    def test_single_string(self):
        self.assertEqual(add_string(['Hello'], 'Hello, {}.'), ['Hello, Hello.'])

    def test_string_without_placeholder(self):
        self.assertEqual(add_string(['Hello', 'World'], 'Hello'), ['Hello', 'World'])

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
            add_string([None], 'Hello, {}.')
