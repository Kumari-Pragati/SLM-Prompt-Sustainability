import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_blank('Hello World', '*'), 'Hello*World')

    def test_edge_case(self):
        self.assertEqual(replace_blank(' ', '*'), '*')

    def test_corner_case(self):
        self.assertEqual(replace_blank('NoSpaces', '*'), 'NoSpaces')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_blank(12345, '*')
