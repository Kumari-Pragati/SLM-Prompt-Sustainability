import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(add_string(['Hello', 'World'], 'Hello, {}.'), ['Hello, Hello.','Hello, World.'])

    def test_empty_list(self):
        self.assertEqual(add_string([], 'Hello, {}.'), [])

    def test_empty_string(self):
        self.assertEqual(add_string(['Hello', 'World'], ''), ['', ''])

    def test_special_characters_in_string(self):
        self.assertEqual(add_string(['Hello', 'World'], 'Hello, {}. How are you, {}?'), 
                         ['Hello, Hello. How are you, Hello?','Hello, World. How are you, World?'])

    def test_special_characters_in_list_elements(self):
        self.assertEqual(add_string(['Hello@', 'World#'], 'Hello, {}.'), 
                         ['Hello, Hello@.','Hello, World#.'])
