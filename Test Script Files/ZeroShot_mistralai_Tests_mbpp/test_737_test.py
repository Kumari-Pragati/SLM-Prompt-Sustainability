import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):

    def test_valid_strings(self):
        test_cases = [
            ("Alice", "Valid"),
            ("a1b2c3", "Valid"),
            ("_My_Name", "Valid"),
            ("A1B2C3", "Valid"),
            ("aeiou", "Valid"),
            ("AEIOU", "Valid"),
        ]
        for string, expected_result in test_cases:
            with self.subTest(f"Testing string '{string}'"):
                self.assertEqual(check_str(string), expected_result)

    def test_invalid_strings(self):
        test_cases = [
            ("123", "Invalid"),
            ("!Alice", "Invalid"),
            ("_123", "Invalid"),
            ("A1b2", "Invalid"),
            ("0A1B2", "Invalid"),
            ("abc", "Invalid"),
            ("ABC", "Invalid"),
            ("#MyName", "Invalid"),
            ("@123", "Invalid"),
            ("789", "Invalid"),
        ]
        for string, expected_result in test_cases:
            with self.subTest(f"Testing string '{string}'"):
                self.assertEqual(check_str(string), expected_result)
