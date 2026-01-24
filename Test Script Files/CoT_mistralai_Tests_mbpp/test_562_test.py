import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Max_Length(['a']), 1)

    def test_multiple_elements_same_length(self):
        self.assertEqual(Find_Max_Length(['aa', 'bb', 'cc']), 2)

    def test_multiple_elements_different_lengths(self):
        self.assertEqual(Find_Max_Length(['aa', 'ab', 'abc']), 3)

    def test_negative_strings(self):
        self.assertEqual(Find_Max_Length(['aa', '-a', 'abc']), 3)

    def test_empty_strings(self):
        self.assertEqual(Find_Max_Length(['', 'aa', 'abc']), 3)

    def test_list_with_non_string_elements(self):
        self.assertEqual(Find_Max_Length(['aa', 1, 'abc']), 3)
