import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_duplicate(""), "")

    def test_single_word(self):
        self.assertEqual(remove_duplicate("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(remove_duplicate("hello world hello"), "hello world")

    def test_duplicates(self):
        self.assertEqual(remove_duplicate("hello hello hello"), "hello")

    def test_empty_string_with_spaces(self):
        self.assertEqual(remove_duplicate("   "), "   ")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_duplicate(123)

    def test_non_string_input_with_spaces(self):
        with self.assertRaises(TypeError):
            remove_duplicate("   123   ")
