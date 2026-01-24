import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Min_Length(['a']), 1)

    def test_list_with_single_word(self):
        self.assertEqual(Find_Min_Length(['hello']), 5)

    def test_list_with_multiple_words(self):
        self.assertEqual(Find_Min_Length(['hello', 'world']), 5)

    def test_list_with_mixed_types(self):
        self.assertEqual(Find_Min_Length(['hello', 1, [2, 3]]), 2)

    def test_list_with_empty_strings(self):
        self.assertEqual(Find_Min_Length(['', ' ', '\t']), 0)
