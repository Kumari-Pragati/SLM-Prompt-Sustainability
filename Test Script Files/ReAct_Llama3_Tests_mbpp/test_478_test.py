import unittest
from mbpp_478_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_lowercase(""), "")

    def test_all_uppercase(self):
        self.assertEqual(remove_lowercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_all_lowercase(self):
        self.assertEqual(remove_lowercase("abcdefghijklmnopqrstuvwxyz"), "")

    def test_mixed_case(self):
        self.assertEqual(remove_lowercase("HelloWorld"), "HW")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase(123)

    def test_non_string_like_input(self):
        with self.assertRaises(TypeError):
            remove_lowercase([1, 2, 3])

    def test_non_string_like_input2(self):
        with self.assertRaises(TypeError):
            remove_lowercase({"a": 1, "b": 2})
