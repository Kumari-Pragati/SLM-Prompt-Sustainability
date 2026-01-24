import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):

    def test_remove_simple_numbers(self):
        self.assertEqual(remove(['123', '456']), ['', ''])

    def test_remove_numbers_in_strings(self):
        self.assertEqual(remove(['abc123def', 'ghi456jkl']), ['abcdef', 'ghi'])

    def test_remove_empty_list(self):
        self.assertEqual(remove([]), [])

    def test_remove_single_number(self):
        self.assertEqual(remove(['123']), [''])

    def test_remove_numbers_with_special_characters(self):
        self.assertEqual(remove(['123@#$', '456^&*']), ['', ''])

    def test_remove_numbers_with_spaces(self):
        self.assertEqual(remove(['123 ', ' 456']), [' ', ''])

    def test_remove_numbers_with_mixed_types(self):
        self.assertEqual(remove(['123', 'abc', '456']), ['', 'abc', ''])
