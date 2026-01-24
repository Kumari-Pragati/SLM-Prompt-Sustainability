import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(remove_dirty_chars("HelloWorld", "!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), "HelloWorld")

    def test_edge_case_empty_strings(self):
        self.assertEqual(remove_dirty_chars("", "!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), "")
        self.assertEqual(remove_dirty_chars("!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", ""), "!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

    def test_edge_case_single_char(self):
        for char in "!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
            self.assertEqual(remove_dirty_chars(char, "!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), char)

    def test_edge_case_different_lengths(self):
        self.assertEqual(remove_dirty_chars("AaBbCc", "!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"), "AaBbCc")
        self.assertEqual(remove_dirty_chars("!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", "AaBbCc"), "!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_dirty_chars(123, "!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        with self.assertRaises(TypeError):
            remove_dirty_chars("!@#$%^&*()_+-=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", 123)
