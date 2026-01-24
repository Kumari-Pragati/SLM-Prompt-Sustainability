import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_max_specialchar("Hello, world.", 1), "Hello: world.")

    def test_no_special_char(self):
        self.assertEqual(replace_max_specialchar("Hello world", 1), "Hello world")

    def test_all_special_chars(self):
        self.assertEqual(replace_max_specialchar(".,", 1), ":")

    def test_more_than_n_special_chars(self):
        self.assertEqual(replace_max_specialchar("Hello, world.", 2), "Hello:, world.")

    def test_n_is_zero(self):
        self.assertEqual(replace_max_specialchar("Hello, world.", 0), "Hello, world.")

    def test_n_is_greater_than_special_chars(self):
        self.assertEqual(replace_max_specialchar("Hello, world.", 5), "Hello:, world.")

    def test_empty_string(self):
        self.assertEqual(replace_max_specialchar("", 1), "")

    def test_invalid_n(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar("Hello, world.", "one")
