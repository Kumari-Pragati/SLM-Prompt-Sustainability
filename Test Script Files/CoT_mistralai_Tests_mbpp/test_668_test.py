import unittest
from mbpp_668_code import replace

class TestReplaceFunction(unittest.TestCase):
    def test_replace_single_char(self):
        self.assertEqual(replace('a', 'x'), 'xx')

    def test_replace_multiple_chars(self):
        self.assertEqual(replace('aa', 'x'), 'xxx')

    def test_replace_empty_string(self):
        self.assertEqual(replace('', 'x'), '')

    def test_replace_string_with_only_one_char(self):
        self.assertEqual(replace('x', 'x'), 'x')

    def test_replace_string_with_longer_pattern(self):
        self.assertEqual(replace('aaaaaa', 'x'), 'xxxxxx')

    def test_replace_string_with_shorter_pattern(self):
        self.assertEqual(replace('xxxxxx', 'x'), 'xx')

    def test_invalid_input_non_string(self):
        self.assertRaises(TypeError, replace, 1, 'x')

    def test_invalid_input_empty_pattern(self):
        self.assertRaises(ValueError, replace, 'xx', '')
