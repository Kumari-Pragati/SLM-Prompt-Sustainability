import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Min_Length(['a']), 1)

    def test_list_with_single_min_length(self):
        self.assertEqual(Find_Min_Length(['ab', 'abc', 'abcd']), 3)

    def test_list_with_multiple_min_lengths(self):
        self.assertEqual(Find_Min_Length(['a', 'ab', 'abc', 'abcd']), 2)

    def test_list_with_mixed_min_lengths(self):
        self.assertEqual(Find_Min_Length(['aa', 'ab', 'abc', 'abcd', 'aab', 'aabc']), 2)
