import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Min_Length(['abc', 'defgh', 'ijkl']), 3)

    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Min_Length(['abcdefgh']), 8)

    def test_all_same_length_elements(self):
        self.assertEqual(Find_Min_Length(['abc', 'abc', 'abc']), 3)

    def test_mixed_length_elements(self):
        self.assertEqual(Find_Min_Length(['abcd', 'ef', 'ghij']), 2)

    def test_list_with_empty_string(self):
        self.assertEqual(Find_Min_Length(['abc', '', 'def']), 0)

    def test_list_with_numeric_strings(self):
        self.assertEqual(Find_Min_Length(['123', '45678', '9']), 1)

    def test_list_with_whitespace_strings(self):
        self.assertEqual(Find_Min_Length(['abc ', 'defgh', 'ijkl']), 3)

    def test_list_with_special_characters(self):
        self.assertEqual(Find_Min_Length(['abc!@#', 'def$%^', 'ghi*()']), 6)
