import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_specialchar("Hello, World."), "Hello:World:")

    def test_edge_case_with_no_special_char(self):
        self.assertEqual(replace_specialchar("HelloWorld"), "HelloWorld")

    def test_edge_case_with_empty_string(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_corner_case_with_multiple_special_chars(self):
        self.assertEqual(replace_specialchar("Hello,,,World.."), "Hello::World:")

    def test_corner_case_with_special_chars_at_start_and_end(self):
        self.assertEqual(replace_specialchar(",Hello,World.,"), ":Hello:World:")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            replace_specialchar(12345)
