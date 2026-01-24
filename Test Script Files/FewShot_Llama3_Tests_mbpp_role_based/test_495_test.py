import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_all_uppercase(self):
        self.assertEqual(remove_lowercase("ABC"), "ABC")

    def test_mixed_case(self):
        self.assertEqual(remove_lowercase("AbC"), "AC")

    def test_all_lowercase(self):
        self.assertEqual(remove_lowercase("abc"), "")

    def test_numbers_and_punctuation(self):
        self.assertEqual(remove_lowercase("Ab1c!"), "1")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)
