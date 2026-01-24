import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Max_Length(["a"]), 1)

    def test_list_with_single_max_length(self):
        self.assertEqual(Find_Max_Length(["ab", "cd"]), 2)

    def test_list_with_multiple_max_length(self):
        self.assertEqual(Find_Max_Length(["ab", "a", "cd", "abc"]), 3)

    def test_list_with_negative_strings(self):
        self.assertEqual(Find_Max_Length(["ab", "-cd", "abc"]), 3)

    def test_list_with_empty_strings(self):
        self.assertEqual(Find_Max_Length(["", "ab", "cd"]), 2)
