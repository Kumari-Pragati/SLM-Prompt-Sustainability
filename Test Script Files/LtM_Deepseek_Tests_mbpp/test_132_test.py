import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_single_character_tuple(self):
        self.assertEqual(tup_string(('a',)), 'a')

    def test_numeric_tuple(self):
        self.assertEqual(tup_string((1, 2, 3)), '123')

    def test_mixed_type_tuple(self):
        self.assertEqual(tup_string(('a', 1, 2.0)), 'a12.0')

    def test_large_tuple(self):
        self.assertEqual(tup_string(('a'*1000,)), 'a'*1000)
