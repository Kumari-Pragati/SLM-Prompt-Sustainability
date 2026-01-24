import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    def test_valid_str(self):
        self.assertEqual(check_str("hello"), "Valid")
        self.assertEqual(check_str("Hello"), "Valid")
        self.assertEqual(check_str("aeiou"), "Valid")
        self.assertEqual(check_str("AEIOU"), "Valid")

    def test_invalid_str(self):
        self.assertEqual(check_str(""), "Invalid")
        self.assertEqual(check_str("123"), "Invalid")
        self.assertEqual(check_str("abc"), "Invalid")
        self.assertEqual(check_str("a"), "Invalid")

    def test_edge_cases(self):
        self.assertEqual(check_str("aeiou123"), "Valid")
        self.assertEqual(check_str("AEIOU_abc"), "Valid")
        self.assertEqual(check_str("hello_world"), "Valid")
        self.assertEqual(check_str("AEIOU"), "Valid")

    def test_regex_pattern(self):
        self.assertEqual(check_str("aeiou"), "Valid")
        self.assertEqual(check_str("AEIOU"), "Valid")
        self.assertEqual(check_str("aeiouAEIOU"), "Valid")
        self.assertEqual(check_str("AEIOUaeiou"), "Valid")
