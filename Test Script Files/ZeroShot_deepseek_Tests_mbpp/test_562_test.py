import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Max_Length(['a']), 1)

    def test_list_with_strings(self):
        self.assertEqual(Find_Max_Length(['abc', 'de', 'fghi']), 4)

    def test_list_with_numbers(self):
        self.assertEqual(Find_Max_Length([123, 45, 6789]), 4)

    def test_list_with_mixed_types(self):
        self.assertEqual(Find_Max_Length(['abc', 123, 'def']), 3)
