import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(tup_string(('x',)), 'x')

    def test_numeric_tuple(self):
        self.assertEqual(tup_string((1, 2, 3)), '123')

    def test_mixed_types_tuple(self):
        self.assertEqual(tup_string(('a', 1, 'b', 2)), 'a1b2')

    def test_special_characters_tuple(self):
        self.assertEqual(tup_string(('!', '@', '#')), '!@#')

    def test_large_tuple(self):
        large_tuple = tuple('a' for _ in range(1000))
        self.assertEqual(tup_string(large_tuple), 'a' * 1000)
