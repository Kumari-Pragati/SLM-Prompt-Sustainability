import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(move_num('a1b2c3'), 'abc123')

    def test_empty_string(self):
        self.assertEqual(move_num(''), '')

    def test_no_digits(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_no_letters(self):
        self.assertEqual(move_num('12345'), '12345')

    def test_single_digit(self):
        self.assertEqual(move_num('a1b'), 'ab1')

    def test_multiple_digits(self):
        self.assertEqual(move_num('a1b2c3d4'), 'abcd1234')

    def test_digits_at_end(self):
        self.assertEqual(move_num('abcd1234'), 'abcd1234')

    def test_special_characters(self):
        self.assertEqual(move_num('a!b@c#123'), 'a!b@c#123')
