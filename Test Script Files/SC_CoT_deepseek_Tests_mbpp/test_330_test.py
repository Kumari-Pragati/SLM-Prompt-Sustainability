import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_char("Hello world"), ['ell', 'orl', 'rld'])

    def test_single_word(self):
        self.assertEqual(find_char("Python"), ['ytho', 'thon'])

    def test_empty_string(self):
        self.assertEqual(find_char(""), [])

    def test_no_words(self):
        self.assertEqual(find_char("1234567890!@#$%^&*()"), [])

    def test_special_characters(self):
        self.assertEqual(find_char("!@#$%^&*()"), [])

    def test_boundary_case(self):
        self.assertEqual(find_char("a"), [])
        self.assertEqual(find_char("abc"), ['b'])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_char(12345)
