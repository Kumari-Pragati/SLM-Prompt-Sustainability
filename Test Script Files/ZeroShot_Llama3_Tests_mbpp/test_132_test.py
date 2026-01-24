import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(tup_string(('a',)), 'a')

    def test_multiple_elements_tuple(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_tuple_with_spaces(self):
        self.assertEqual(tup_string(('a', 'b', 'c ', 'd')), 'abc d')

    def test_tuple_with_punctuation(self):
        self.assertEqual(tup_string((',', '.', '!')), '.,!')
