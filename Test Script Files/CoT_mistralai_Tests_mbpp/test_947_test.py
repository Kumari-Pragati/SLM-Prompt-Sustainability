import unittest
from947_code import len_log

class TestLenLog(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(len_log([]), 0)

    def test_single_element_list(self):
        self.assertEqual(len_log(['a']), 1)

    def test_multiple_elements_same_length(self):
        self.assertEqual(len_log(['aa', 'bb', 'cc']), 2)

    def test_multiple_elements_different_lengths_min_length_first(self):
        self.assertEqual(len_log(['aa', 'ab', 'ac']), 2)

    def test_multiple_elements_different_lengths_min_length_last(self):
        self.assertEqual(len_log(['ac', 'ab', 'aa']), 2)

    def test_negative_list_elements(self):
        self.assertEqual(len_log(['-a', '-b', '-c']), 1)

    def test_empty_string_elements(self):
        self.assertEqual(len_log(['', 'a', 'b']), 1)

    def test_list_with_none(self):
        self.assertEqual(len_log(['a', None, 'b']), 1)

    def test_list_with_numbers(self):
        self.assertEqual(len_log([1, 2, 3]), 1)

    def test_list_with_mixed_types(self):
        self.assertEqual(len_log(['a', 1, 'b', 2.0, None]), 1)
