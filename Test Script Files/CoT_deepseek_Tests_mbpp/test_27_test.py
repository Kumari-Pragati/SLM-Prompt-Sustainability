import unittest
from mbpp_27_code import remove

class TestRemove(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove(['abc123', 'def456']), ['abc', 'def'])

    def test_empty_list(self):
        self.assertEqual(remove([]), [])

    def test_list_with_no_numbers(self):
        self.assertEqual(remove(['abc', 'def']), ['abc', 'def'])

    def test_list_with_all_numbers(self):
        self.assertEqual(remove(['123', '456']), ['', ''])

    def test_list_with_mixed_characters_and_numbers(self):
        self.assertEqual(remove(['abc123def', 'ghi456jkl']), ['abcdef', 'ghi456jkl'])

    def test_list_with_special_characters(self):
        self.assertEqual(remove(['abc!123', 'def@456']), ['abc', 'def'])

    def test_list_with_mixed_case_numbers(self):
        self.assertEqual(remove(['Abc123', 'Def456']), ['Abc', 'Def'])
