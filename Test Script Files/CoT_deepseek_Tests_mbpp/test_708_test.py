import unittest
from mbpp_708_code import Convert

class TestConvertFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Convert('Hello World'), ['Hello', 'World'])

    def test_single_word(self):
        self.assertEqual(Convert('Python'), ['Python'])

    def test_empty_string(self):
        self.assertEqual(Convert(''), [])

    def test_multiple_spaces(self):
        self.assertEqual(Convert('Hello     World'), ['Hello', 'World'])

    def test_trailing_spaces(self):
        self.assertEqual(Convert('Hello World '), ['Hello', 'World'])

    def test_leading_spaces(self):
        self.assertEqual(Convert(' Hello World'), ['Hello', 'World'])

    def test_mixed_spaces_and_tabs(self):
        self.assertEqual(Convert('Hello\tWorld'), ['Hello', 'World'])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            Convert(None)
