import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_simple_digits(self):
        self.assertEqual(move_num("12345"), "12345")
        self.assertEqual(move_999_999_999("1234567890123"), "12345678901231234567890")

    def test_empty_string(self):
        self.assertEqual(move_num(""), "")

    def test_only_letters(self):
        self.assertEqual(move_num("abcdefg"), "abcdefg")

    def test_mixed_case(self):
        self.assertEqual(move_num("AbCd123EfG456"), "AbCdEfG456123")

    def test_leading_digits(self):
        self.assertEqual(move_num("123abc"), "123abc")
        self.assertEqual(move_num("1234567890"), "1234567890")

    def test_trailing_digits(self):
        self.assertEqual(move_num("abc123"), "abc123")
        self.assertEqual(move_num("abc1234567890"), "abc1234567890")

    def test_multiple_digits(self):
        self.assertEqual(move_num("12345678901234567890"), "12345678901234567890")

    def test_negative_numbers(self):
        self.assertEqual(move_num("-123"), "-123")
        self.assertEqual(move_num("-1234567890"), "-1234567890")
