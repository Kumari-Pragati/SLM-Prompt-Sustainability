import unittest

from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Max_Length(['abc', 'defgh', 'ijklm']), 5)

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element(self):
        self.assertEqual(Find_Max_Length(['abc']), 3)

    def test_longest_string_at_end(self):
        self.assertEqual(Find_Max_Length(['abc', 'def', 'ghijk']), 5)

    def test_longest_string_at_start(self):
        self.assertEqual(Find_Max_Length(['abcdefg', 'h', 'i']), 7)

    def test_special_characters(self):
        self.assertEqual(Find_Max_Length(['abc!@#', 'def^&*', 'ghi(**)']), 7)

    def test_numeric_strings(self):
        self.assertEqual(Find_Max_Length(['12345', '67890', '1']), 5)

    def test_empty_strings(self):
        self.assertEqual(Find_Max_Length(['', ' ', '   ']), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Find_Max_Length(12345)
