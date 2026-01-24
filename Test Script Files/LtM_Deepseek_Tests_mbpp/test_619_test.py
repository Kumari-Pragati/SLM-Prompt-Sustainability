import unittest
from mbpp_619_code import move_num

class TestMoveNum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(move_num('a1b2c3'), 'abc123')

    def test_empty_input(self):
        self.assertEqual(move_num(''), '')

    def test_input_with_no_digits(self):
        self.assertEqual(move_num('abc'), 'abc')

    def test_input_with_only_digits(self):
        self.assertEqual(move_num('123'), '123')

    def test_input_with_special_characters(self):
        self.assertEqual(move_num('a!b@c#'), 'a!b@c#')

    def test_input_with_mixed_characters_and_digits(self):
        self.assertEqual(move_num('a1b2!c3@'), 'a!b@c123')
