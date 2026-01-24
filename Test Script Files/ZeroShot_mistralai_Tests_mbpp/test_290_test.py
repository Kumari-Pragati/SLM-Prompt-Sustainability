import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(max_length(['a']), (1, 'a'))

    def test_list_with_multiple_elements(self):
        self.assertEqual(max_length(['aa', 'ab', 'ac']), (2, 'ac'))

    def test_list_with_mixed_types(self):
        self.assertEqual(max_length(['a', 1, 'b']), (2, 'b'))

    def test_list_with_empty_strings(self):
        self.assertEqual(max_length(['', 'a', '']), (2, 'a'))

    def test_list_with_long_strings(self):
        self.assertEqual(max_length(['abc', 'abcd', 'abcdabcd'])), (8, 'abcdabcd'))
