import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_specialchar("Hello, world."), "Hello:world:")

    def test_no_special_char(self):
        self.assertEqual(replace_specialchar("Hello world"), "Hello world")

    def test_empty_string(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_special_char_at_start_and_end(self):
        self.assertEqual(replace_specialchar(",Hello, world."), ":Hello:world:")

    def test_special_char_only(self):
        self.assertEqual(replace_specialchar(",."), ":")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            replace_specialchar(None)
