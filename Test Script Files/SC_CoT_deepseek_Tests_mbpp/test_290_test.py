import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_length(['abc', 'de', 'fghi']), (4, 'fghi'))

    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, ''))

    def test_list_with_one_element(self):
        self.assertEqual(max_length(['abc']), (3, 'abc'))

    def test_list_with_same_length_elements(self):
        self.assertEqual(max_length(['abc', 'def', 'ghi']), (3, 'ghi'))

    def test_list_with_long_strings(self):
        self.assertEqual(max_length(['abcdefgh', 'ijklmnop']), (8, 'abcdefgh'))

    def test_list_with_empty_strings(self):
        self.assertEqual(max_length(['', ' ']), (1, ' '))

    def test_list_with_numeric_strings(self):
        self.assertEqual(max_length(['12345', '6789']), (5, '12345'))

    def test_list_with_special_characters(self):
        self.assertEqual(max_length(['!@#$%^', '&*()']), (6, '!@#$%^'))

    def test_list_with_mixed_case_strings(self):
        self.assertEqual(max_length(['AbC', 'dEf', 'GHi']), (3, 'GHi'))

    def test_list_with_mixed_length_strings(self):
        self.assertEqual(max_length(['abc', 'de', 'fgh', 'i']), (3, 'fgh'))
