import unittest
from mbpp_668_code import replace

class TestReplaceFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace('hello world', 'l'), 'helo world')

    def test_edge_case_single_char(self):
        self.assertEqual(replace('hello world', 'o'), 'hell wrld')

    def test_edge_case_no_char(self):
        self.assertEqual(replace('hello world', ''), 'hello world')

    def test_edge_case_repeated_char(self):
        self.assertEqual(replace('helllllo', 'l'), 'helo')

    def test_error_case_none_string(self):
        with self.assertRaises(TypeError):
            replace(123, 'l')

    def test_error_case_none_char(self):
        with self.assertRaises(TypeError):
            replace('hello world', 123)
