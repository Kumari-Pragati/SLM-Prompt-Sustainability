import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(max_run_uppercase(""), 0)

    def test_all_uppercase(self):
        self.assertEqual(max_run_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)

    def test_all_lowercase(self):
        self.assertEqual(max_run_uppercase("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_mixed_case(self):
        self.assertEqual(max_run_uppercase("AbCdEfGhIjKlMnOpQrStUvWxYz"), 5)

    def test_single_uppercase(self):
        self.assertEqual(max_run_uppercase("HelloWorld"), 1)

    def test_single_lowercase(self):
        self.assertEqual(max_run_uppercase("hello world"), 0)

    def test_multiple_uppercase(self):
        self.assertEqual(max_run_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)

    def test_multiple_lowercase(self):
        self.assertEqual(max_run_uppercase("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_edge_case(self):
        self.assertEqual(max_run_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"), 26)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_run_uppercase(123)
