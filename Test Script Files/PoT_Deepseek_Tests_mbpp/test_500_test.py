import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_elements(['a', 'b', 'c']), ' a b c')

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]), '')

    def test_single_element(self):
        self.assertEqual(concatenate_elements(['hello']), ' hello')

    def test_whitespace_in_elements(self):
        self.assertEqual(concatenate_elements(['a', 'b ', 'c']), ' a b  c')

    def test_empty_string_elements(self):
        self.assertEqual(concatenate_elements(['', 'b', 'c']), '  b c')

    def test_large_list(self):
        large_list = ['a'] * 1000
        expected_output = ' ' + ' a'.join(large_list)
        self.assertEqual(concatenate_elements(large_list), expected_output)
