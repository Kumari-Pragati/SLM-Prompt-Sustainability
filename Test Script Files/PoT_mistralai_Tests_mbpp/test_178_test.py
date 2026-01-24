import unittest
from mbpp_178_code import string_literals

class TestStringLiterals(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(string_literals(['abc', 'def'], 'abcdef'), 'Matched!')
        self.assertEqual(string_literals(['abc', 'def'], 'abcd'), 'Matched!')
        self.assertEqual(string_literals(['abc', 'def'], 'abcdg'), 'Not Matched!')

    def test_edge_case(self):
        self.assertEqual(string_literals(['', 'def'], 'abcdef'), 'Not Matched!')
        self.assertEqual(string_literals(['abc', ''], 'abcdef'), 'Matched!')
        self.assertEqual(string_literals(['', ''], 'abcdef'), 'Not Matched!')

    def test_boundary_case(self):
        self.assertEqual(string_literals(['a', 'z'], 'az'), 'Matched!')
        self.assertEqual(string_literals(['a', 'z'], 'aa'), 'Not Matched!')
        self.assertEqual(string_literals(['a', 'z'], 'zz'), 'Matched!')

    def test_invalid_input(self):
        self.assertRaises(TypeError, string_literals, [1, 2], 'abcdef')
        self.assertRaises(TypeError, string_literals, ['abc', 2], 'abcdef')
