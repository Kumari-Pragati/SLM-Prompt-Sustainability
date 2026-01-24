import unittest
from mbpp_562_code import Find_Max_Length

class TestFind_Max_Length(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry"]), 7)

    def test_edge_case_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Max_Length(["hello"]), 5)

    def test_edge_case_single_element_list_with_spaces(self):
        self.assertEqual(Find_Max_Length(["hello world"]), 11)

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry", "date"]), 7)

    def test_edge_case_multiple_elements_list_with_spaces(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry", "date", "elderberry"]), 12)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "apple", "cherry"]), 7)

    def test_edge_case_list_with_duplicates_and_spaces(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "apple", "cherry", "date"]), 8)
