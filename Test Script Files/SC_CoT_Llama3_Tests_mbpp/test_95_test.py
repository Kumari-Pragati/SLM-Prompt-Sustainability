import unittest
from mbpp_95_code import Find_Min_Length

class TestFind_Min_Length(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry"]), 5)

    def test_edge_case_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Min_Length(["hello"]), 5)

    def test_edge_case_single_element_list_with_spaces(self):
        self.assertEqual(Find_Min_Length(["hello world"]), 11)

    def test_edge_case_multiple_elements_list(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry", "date"]), 5)

    def test_edge_case_multiple_elements_list_with_spaces(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry", "date", "elderberry"]), 8)

    def test_edge_case_empty_string(self):
        self.assertEqual(Find_Min_Length([""]), 0)

    def test_edge_case_single_element_empty_string(self):
        self.assertEqual(Find_Min_Length([""]), 0)

    def test_edge_case_multiple_elements_empty_strings(self):
        self.assertEqual(Find_Min_Length(["", "", ""]), 0)

    def test_edge_case_multiple_elements_empty_strings_and_non_empty(self):
        self.assertEqual(Find_Min_Length(["", "apple", "", "banana"]), 5)

    def test_edge_case_non_empty_string(self):
        self.assertEqual(Find_Min_Length(["hello"]), 5)

    def test_edge_case_multiple_elements_non_empty_strings(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry"]), 5)

    def test_edge_case_multiple_elements_non_empty_strings_and_empty(self):
        self.assertEqual(Find_Min_Length(["apple", "", "banana", "cherry"]), 5)

    def test_edge_case_multiple_elements_non_empty_strings_and_empty_and_spaces(self):
        self.assertEqual(Find_Min_Length(["apple", "", "banana", "cherry", "date"]), 5)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            Find_Min_Length(None)
