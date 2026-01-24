import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(move_num(''), '')

    def test_only_digits(self):
        self.assertEqual(move_num('12345'), '12345')

    def test_only_letters(self):
        self.assertEqual(move_num('abcde'), 'abcde')

    def test_mixed_case(self):
        self.assertEqual(move_num('AbCd123Ef'), 'AbCdEf123')

    def test_leading_digits(self):
        self.assertEqual(move_num('12abc345'), '12345abc')

    def test_trailing_digits(self):
        self.assertEqual(move_num('abc123'), 'abc123')

    def test_multiple_digits(self):
        self.assertEqual(move_num('ab1c2d3'), 'abcd312')
