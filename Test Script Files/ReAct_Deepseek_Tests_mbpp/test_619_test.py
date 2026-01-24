import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(move_num('a1b2c3'), 'ab1c23')

    def test_empty_string(self):
        self.assertEqual(move_num(''), '')

    def test_string_with_no_digits(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_string_with_only_digits(self):
        self.assertEqual(move_num('123'), '123')

    def test_string_with_mixed_digits_and_letters(self):
        self.assertEqual(move_num('a1b2c3d4'), 'abcd1234')

    def test_string_with_leading_digits(self):
        self.assertEqual(move_num('12a3b4'), '12ab34')

    def test_string_with_trailing_digits(self):
        self.assertEqual(move_num('a1b2c34'), 'ab1c234')

    def test_string_with_consecutive_digits(self):
        self.assertEqual(move_num('a12b34c56'), 'a12b34c56')
