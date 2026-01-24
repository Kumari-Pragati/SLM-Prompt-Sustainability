import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_blank('Hello World', '_'), 'Hello_World')

    def test_edge_condition(self):
        self.assertEqual(replace_blank(' ', '_'), '_')

    def test_boundary_condition(self):
        self.assertEqual(replace_blank('a'*201, '_'), 'a'*200 + '_')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_blank(12345, '_')
