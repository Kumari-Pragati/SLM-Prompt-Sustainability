import unittest
from mbpp_178_code import search
from seventeen_eight_code import string_literals

class TestStringLiterals(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(string_literals(['abc', 'def'], 'abcdef'), 'Matched!')

    def test_edge_case_start(self):
        self.assertEqual(string_literals(['abc', 'def'], 'abcd'), 'Matched!')
        self.assertEqual(string_literals(['abc', 'def'], 'abce'), 'Not Matched!')

    def test_edge_case_end(self):
        self.assertEqual(string_literals(['abc', 'def'], 'abcde'), 'Matched!')
        self.assertEqual(string_literals(['abc', 'def'], 'abc'), 'Not Matched!')

    def test_edge_case_both(self):
        self.assertEqual(string_literals(['abc', 'def'], 'abcd'), 'Matched!')
        self.assertEqual(string_literals(['abc', 'def'], 'abcde'), 'Matched!')
        self.assertEqual(string_literals(['abc', 'def'], 'abce'), 'Not Matched!')
        self.assertEqual(string_literals(['abc', 'def'], 'abc'), 'Not Matched!')

    def test_empty_patterns(self):
        self.assertEqual(string_literals([], 'abcdef'), 'Not Matched!')

    def test_empty_text(self):
        self.assertEqual(string_literals(['abc'], ''), 'Not Matched!')

    def test_invalid_input_patterns(self):
        self.assertRaises(TypeError, string_literals, [123, 'def'], 'abcdef')
        self.assertRaises(TypeError, string_literals, ['abc', 123], 'abcdef')

    def test_invalid_input_text(self):
        self.assertRaises(TypeError, string_literals, ['abc', 'def'], 12345)
