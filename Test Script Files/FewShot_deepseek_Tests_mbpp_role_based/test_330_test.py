import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_char("Hello world"), ['Hello', 'world'])

    def test_edge_condition(self):
        self.assertEqual(find_char("a"), ['a'])

    def test_boundary_condition(self):
        self.assertEqual(find_char("abcdefghijklmnopqrstuvwxyz"), ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyz'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_char(123)
