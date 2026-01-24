import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_blank('Hello World', '_'), 'Hello_World')

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_blank('', '_'), '')

    def test_edge_case_no_spaces(self):
        self.assertEqual(replace_blank('HelloWorld', '_'), 'HelloWorld')

    def test_edge_case_single_space(self):
        self.assertEqual(replace_blank(' ', '_'), '_')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            replace_blank(12345, '_')

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            replace_blank('Hello World', None)
