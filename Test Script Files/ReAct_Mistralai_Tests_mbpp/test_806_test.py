import unittest
from mbpp_806_code import max_run_uppercase

class TestMaxRunUppercase(unittest.TestCase):

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertEqual(max_run_uppercase(""), 0)

    def test_all_uppercase(self):
        """Test with a string containing only uppercase letters"""
        self.assertEqual(max_run_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 26)

    def test_all_lowercase(self):
        """Test with a string containing only lowercase letters"""
        self.assertEqual(max_run_uppercase("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_mixed_case(self):
        """Test with a string containing a mix of uppercase and lowercase letters"""
        self.assertEqual(max_run_uppercase("AbCdEfGhIjKlMnOpQrStUvWxYz"), 10)

    def test_single_uppercase(self):
        """Test with a string containing a single uppercase letter"""
        self.assertEqual(max_run_uppercase("A"), 1)

    def test_single_lowercase(self):
        """Test with a string containing a single lowercase letter"""
        self.assertEqual(max_run_uppercase("a"), 0)

    def test_long_string(self):
        """Test with a long string containing a mix of uppercase and lowercase letters"""
        long_string = "A" * 100 + "a" * 100 + "B" * 100 + "b" * 100
        self.assertEqual(max_run_uppercase(long_string), 200)

    def test_leading_uppercase(self):
        """Test with a string starting with an uppercase letter"""
        self.assertEqual(max_run_uppercase("ABCabc"), 2)

    def test_trailing_uppercase(self):
        """Test with a string ending with an uppercase letter"""
        self.assertEqual(max_run_uppercase("abcABC"), 2)

    def test_leading_and_trailing_uppercase(self):
        """Test with a string starting and ending with an uppercase letter"""
        self.assertEqual(max_run_uppercase("ABCabcABC"), 3)

    def test_error_empty_input(self):
        """Test error handling for empty input"""
        with self.assertRaises(TypeError):
            max_run_uppercase(None)
