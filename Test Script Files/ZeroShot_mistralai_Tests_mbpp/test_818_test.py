import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(lower_ctr(''), 0)

    def test_all_uppercase(self):
        self.assertEqual(lower_ctr('HELLO'), 0)

    def test_mixed_case(self):
        self.assertEqual(lower_ctr('Hello World'), 5)

    def test_special_characters(self):
        self.assertEqual(lower_ctr('!Hello World$'), 5)

    def test_punctuation_at_start_and_end(self):
        self.assertEqual(lower_ctr('.,Hello World.'), 5)

    def test_multiple_spaces(self):
        self.assertEqual(lower_ctr('   Hello World   '), 5)

    def test_multiple_whitespace_characters(self):
        self.assertEqual(lower_ctr('\tHello World\n'), 5)
