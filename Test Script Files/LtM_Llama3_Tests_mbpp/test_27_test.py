import unittest
from mbpp_27_code import remove

class TestRemove(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove(['123']), [''])

    def test_multiple_elements_list(self):
        self.assertEqual(remove(['123', 'abc', '456']), ['', 'abc', ''])

    def test_list_with_no_numbers(self):
        self.assertEqual(remove(['abc', 'def']), ['abc', 'def'])

    def test_list_with_no_strings(self):
        self.assertEqual(remove(['123', '456']), ['', ''])

    def test_list_with_mixed_types(self):
        self.assertEqual(remove(['123', 'abc', 123, 'def']), ['', 'abc', '', 'def'])

    def test_list_with_empty_strings(self):
        self.assertEqual(remove(['', 'abc', '']), ['', 'abc', ''])

    def test_list_with_empty_string_and_numbers(self):
        self.assertEqual(remove(['', '123', '456']), ['', '', ''])

    def test_list_with_empty_string_and_strings(self):
        self.assertEqual(remove(['', 'abc', 'def']), ['', 'abc', 'def'])

    def test_list_with_empty_string_and_mixed_types(self):
        self.assertEqual(remove(['', '123', 'abc', 'def']), ['', '', 'abc', 'def'])
