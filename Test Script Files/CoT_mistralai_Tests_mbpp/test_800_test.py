import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_all_spaces(''), '')

    def test_single_space(self):
        self.assertEqual(remove_all_spaces(' '), '')

    def test_multiple_spaces(self):
        self.assertEqual(remove_all_spaces('   test   '), 'test')

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_all_spaces(' test   '), 'test')
        self.assertEqual(remove_all_spaces('  test  '), 'test')

    def test_tab_spaces(self):
        self.assertEqual(remove_all_spaces('\t test \t'), 'test')

    def test_mixed_spaces_and_characters(self):
        self.assertEqual(remove_all_spaces('test 123 456'), 'test123456')

    def test_non_string_input(self):
        self.assertRaises(TypeError, remove_all_spaces, 123)

    def test_string_with_non_printable_characters(self):
        text = '\u0001test\u0002'
        self.assertEqual(remove_all_spaces(text), '\u0001test\u0002')
