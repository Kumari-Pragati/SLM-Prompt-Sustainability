import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):
    def test_single_uppercase(self):
        self.assertEqual(max_run_uppercase("Hello"), 1)

    def test_multiple_uppercase(self):
        self.assertEqual(max_run_uppercase("HELLO WORLD"), 2)

    def test_single_lowercase(self):
        self.assertEqual(max_run_uppercase("hello"), 0)

    def test_multiple_lowercase(self):
        self.assertEqual(max_run_uppercase("hello world"), 0)

    def test_mixed_case(self):
        self.assertEqual(max_run_uppercase("HelloWorld"), 2)

    def test_empty_string(self):
        self.assertEqual(max_run_uppercase(""), 0)

    def test_single_space(self):
        self.assertEqual(max_run_uppercase(" "), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_run_uppercase(123)
