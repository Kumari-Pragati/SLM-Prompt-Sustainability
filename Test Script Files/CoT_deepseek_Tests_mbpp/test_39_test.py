import unittest
from mbpp_39_code import rearange_string

class RearangeStringTestCase(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearange_string('aab'), 'aba')

    def test_single_char(self):
        self.assertEqual(rearange_string('a'), 'a')

    def test_empty_string(self):
        self.assertEqual(rearange_string(''), '')

    def test_string_with_same_chars(self):
        self.assertEqual(rearange_string('aaa'), 'aaa')

    def test_string_with_different_chars(self):
        self.assertEqual(rearange_string('abc'), 'abc')

    def test_string_with_more_than_half_chars(self):
        self.assertEqual(rearange_string('aabbcc'), 'aabbcc')

    def test_string_with_less_than_half_chars(self):
        self.assertEqual(rearange_string('aabbc'), 'ababc')

    def test_string_with_equal_chars(self):
        self.assertEqual(rearange_string('aabbccdd'), 'abcdabcd')

    def test_string_with_unequal_chars(self):
        self.assertEqual(rearange_string('aabbccddde'), '')

    def test_string_with_special_chars(self):
        self.assertEqual(rearange_string('aabbccddeeff'), 'abcdefabcdef')

    def test_string_with_numbers(self):
        self.assertEqual(rearange_string('1223334444'), '1223334444')

    def test_string_with_special_chars_and_numbers(self):
        self.assertEqual(rearange_string('1223334444!@#$'), '1223334444!@#$')

    def test_string_with_special_chars_and_numbers_and_spaces(self):
        self.assertEqual(rearange_string('1223334444!@#$ '), '1223334444!@#$ ')
