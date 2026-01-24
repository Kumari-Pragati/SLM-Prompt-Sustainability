import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_string_list(['abc', 'def']), ['cba', 'fed'])

    def test_empty_list(self):
        self.assertEqual(reverse_string_list([]), [])

    def test_single_string(self):
        self.assertEqual(reverse_string_list(['hello']), ['olleh'])

    def test_long_string(self):
        self.assertEqual(reverse_string_list(['a'*1000]), ['a'*1000][::-1])

    def test_string_with_spaces(self):
        self.assertEqual(reverse_string_list(['hello world']), ['dlrow olleh'])

    def test_string_with_special_characters(self):
        self.assertEqual(reverse_string_list(['hello@world']), ['dlrow@olleh'])

    def test_string_with_numbers(self):
        self.assertEqual(reverse_string_list(['123456']), ['654321'])
