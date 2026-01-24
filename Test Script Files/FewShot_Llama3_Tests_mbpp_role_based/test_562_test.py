import unittest
from mbpp_562_code import Find_Max_Length

class TestFind_Max_Length(unittest.TestCase):
    def test_typical_use_case(self):
        lst = ["apple", "banana", "cherry"]
        self.assertEqual(Find_Max_Length(lst), 7)

    def test_empty_list(self):
        lst = []
        self.assertEqual(Find_Max_Length(lst), 0)

    def test_single_element_list(self):
        lst = ["hello"]
        self.assertEqual(Find_Max_Length(lst), 5)

    def test_multiple_max_length_elements(self):
        lst = ["apple", "banana", "cherry", "date"]
        self.assertEqual(Find_Max_Length(lst), 7)

    def test_list_with_non_string_elements(self):
        lst = [1, 2, 3, "hello", "world"]
        self.assertEqual(Find_Max_Length(lst), 5)

    def test_list_with_mixed_case_elements(self):
        lst = ["Hello", "WORLD", "abc", "def"]
        self.assertEqual(Find_Max_Length(lst), 6)
