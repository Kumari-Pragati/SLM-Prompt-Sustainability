import unittest
from mbpp_562_code import Find_Max_Length

class TestFind_Max_Length(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry"]), 7)

    def test_empty_input(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element_input(self):
        self.assertEqual(Find_Max_Length(["hello"]), 5)

    def test_multiple_elements_input(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry", "date"]), 7)

    def test_longest_string_input(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry", "date", "dragonfruit"]), 13)

    def test_max_length_of_all_strings_input(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry", "date", "dragonfruit", "elephant"]), 13)
