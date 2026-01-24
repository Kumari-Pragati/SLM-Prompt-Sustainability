import unittest
from mbpp_95_code import Find_Min_Length

class TestFind_Min_Length(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry"]), 5)

    def test_empty_input(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_single_element_input(self):
        self.assertEqual(Find_Min_Length(["hello"]), 5)

    def test_multiple_elements_input(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry", "date"]), 5)

    def test_longest_element_input(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry", "date", "elephant"]), 8)

    def test_all_elements_of_same_length(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry", "date", "apple"]), 5)

    def test_all_elements_of_different_lengths(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry", "date", "elephant", "grape"]), 5)
