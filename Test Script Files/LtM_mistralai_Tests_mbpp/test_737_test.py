import unittest
from mbpp_737_code import check_str

class TestCheckStr(unittest.TestCase):
    def test_simple_valid(self):
        self.assertEqual(check_str("a"), "Valid")
        self.assertEqual(check_str("A"), "Valid")
        self.assertEqual(check_str("_"), "Valid")
        self.assertEqual(check_str("_123"), "Valid")
        self.assertEqual(check_str("_abc"), "Valid")
        self.assertEqual(check_str("_AbC"), "Valid")

    def test_edge_cases(self):
        self.assertEqual(check_str(""), "Invalid")
        self.assertEqual(check_str(" "), "Invalid")
        self.assertEqual(check_str("aeiou"), "Valid")
        self.assertEqual(check_str("aeiouAEIOU"), "Valid")
        self.assertEqual(check_str("aeiouAEIOU_"), "Valid")
        self.assertEqual(check_str("aeiouAEIOU_123"), "Valid")
        self.assertEqual(check_str("aeiouAEIOU_123_"), "Valid")
        self.assertEqual(check_str("aeiouAEIOU_123_456"), "Valid")
        self.assertEqual(check_str("aeiouAEIOU_123_456_789"), "Valid")
        self.assertEqual(check_str("aeiouAEIOU_123_456_789_012"), "Invalid")
        self.assertEqual(check_str("aeiouAEIOU_123_456_789_0123"), "Invalid")
