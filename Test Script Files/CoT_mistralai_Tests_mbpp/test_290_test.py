import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(max_length(['a']), (1, 'a'))

    def test_list_with_single_max_length(self):
        self.assertEqual(max_length(['ab', 'cd', 'ef']), (3, 'ef'))

    def test_list_with_multiple_max_length(self):
        self.assertEqual(max_length(['ab', 'cd', 'a', 'ef']), (2, 'cd'))

    def test_list_with_mixed_types(self):
        self.assertEqual(max_length(['ab', 123, 'cd']), (2, 'ab'))

    def test_list_with_empty_strings(self):
        self.assertEqual(max_length(['', 'ab', 'cd']), (2, 'ab'))

    def test_list_with_negative_length(self):
        self.assertEqual(max_length(['--', '-', '--']) , (2, '-'))
