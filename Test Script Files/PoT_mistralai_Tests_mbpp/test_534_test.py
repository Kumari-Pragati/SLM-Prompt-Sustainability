import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(search_literal('abc', 'abcaaaabc'), (1, 3))
        self.assertEqual(search_literal('xyz', 'xyzyyzxyz'), (0, 3))
        self.assertEqual(search_literal('123', '1234567890123'), (8, 11))

    def test_edge_case(self):
        self.assertEqual(search_literal('abc', 'abcaaaaabc'), (1, 4))
        self.assertEqual(search_literal('xyz', 'xyzyyzxyzz'), (0, 3))
        self.assertEqual(search_literal('123', '12345678901223'), (8, 11))

    def test_boundary_case(self):
        self.assertEqual(search_literal('abc', 'a'), (0, 1))
        self.assertEqual(search_literal('xyz', 'xyz'), (0, 3))
        self.assertEqual(search_literal('123', '123'), (0, 3))
        self.assertEqual(search_literal('abc', 'abcdefg'), (1, 4))
        self.assertEqual(search_literal('xyz', 'xyzabc'), (0, 3))
        self.assertEqual(search_literal('123', '1234'), (0, 3))

    def test_empty_text(self):
        self.assertIsNone(search_literal('abc', ''))

    def test_empty_pattern(self):
        self.assertIsNone(search_literal('', 'abcaaaabc'))

    def test_non_string_input(self):
        self.assertRaises(TypeError, search_literal, 123, 'abcaaaabc')
        self.assertRaises(TypeError, search_literal, 'abc', 123)
