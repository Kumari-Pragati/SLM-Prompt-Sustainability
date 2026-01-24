import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_charac(""), 0)

    def test_single_char(self):
        self.assertEqual(count_charac("a"), 1)

    def test_multiple_chars(self):
        self.assertEqual(count_charac("abc"), 3)

    def test_spaces(self):
        self.assertEqual(count_charac("   "), 3)

    def test_punctuation(self):
        self.assertEqual(count_charac(".,!"), 3)

    def test_mixed_chars(self):
        self.assertEqual(count_charac("abc123!"), 6)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_charac(123)
