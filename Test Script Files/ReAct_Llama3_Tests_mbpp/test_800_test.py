import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_all_spaces(""), "")

    def test_single_space(self):
        self.assertEqual(remove_all_spaces(" "), "")

    def test_multiple_spaces(self):
        self.assertEqual(remove_all_spaces("   "), "")

    def test_spaces_at_start_and_end(self):
        self.assertEqual(remove_all_spaces("   hello   "), "hello")

    def test_spaces_in_between_words(self):
        self.assertEqual(remove_all_spaces("hello   world"), "helloworld")

    def test_spaces_and_punctuation(self):
        self.assertEqual(remove_all_spaces("hello, world!"), "hello,world!")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_all_spaces(123)

    def test_non_string_input_with_default(self):
        self.assertEqual(remove_all_spaces(None), "")
