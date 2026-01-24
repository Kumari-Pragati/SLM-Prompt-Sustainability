import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):

    def test_empty_string(self):
        """Test case for an empty string"""
        result = count_alpha_dig_spl("")
        self.assertEqual(result, (0, 0, 0))

    def test_all_alphabets(self):
        """Test case for a string containing only alphabets"""
        result = count_alpha_dig_spl("abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(result, (26, 0, 0))

    def test_all_digits(self):
        """Test case for a string containing only digits"""
        result = count_alpha_dig_spl("1234567890")
        self.assertEqual(result, (0, 10, 0))

    def test_all_special_characters(self):
        """Test case for a string containing only special characters"""
        result = count_alpha_dig_spl("!@#$%^&*()_+-={}|[]\:;'<>,.?/")
        self.assertEqual(result, (0, 0, 33))

    def test_mixed_case_string(self):
        """Test case for a string containing mixed case alphabets"""
        result = count_alpha_dig_spl("AbCdEfGhIjKlMnOpQrStUvWxYz")
        self.assertEqual(result, (26, 0, 0))

    def test_mixed_string(self):
        """Test case for a string containing mixed alphabets, digits, and special characters"""
        result = count_alpha_dig_spl("AbCd123!@#$%^&*()_+-={}|[]\:;'<>,.?/")
        self.assertEqual(result, (10, 3, 22))

    def test_long_string(self):
        """Test case for a long string to ensure function handles large inputs correctly"""
        result = count_alpha_dig_spl("a" * 1000 + "1" * 1000 + "!" * 1000)
        self.assertEqual(result, (1000, 1000, 1000))

    def test_short_string(self):
        """Test case for a short string to ensure function handles small inputs correctly"""
        result = count_alpha_dig_spl("a" + "1" + "!")
        self.assertEqual(result, (1, 1, 1))
