import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(tup_string(('a',)), 'a')

    def test_multiple_elements_tuple(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_mixed_types_tuple(self):
        self.assertRaises(TypeError, tup_string, (1, 'a', 3.14))

    def test_string_as_tuple(self):
        self.assertEqual(tup_string(('Hello', 'World')), 'HelloWorld')
