import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(min_length_list([]), (0, []))

    def test_single_element_list(self):
        self.assertEqual(min_length_list(['hello']), (5, ['hello']))

    def test_multiple_elements_list(self):
        self.assertEqual(min_length_list(['hello', 'world', 'abc']), (3, ['abc']))

    def test_list_with_duplicates(self):
        self.assertEqual(min_length_list(['hello', 'world', 'abc', 'abc']), (3, ['abc']))

    def test_list_with_empty_strings(self):
        self.assertEqual(min_length_list(['hello', '', 'world']), (5, 'hello'))

    def test_list_with_mixed_lengths(self):
        self.assertEqual(min_length_list(['hello', 'world', 'abc','short']), (4,'short'))
