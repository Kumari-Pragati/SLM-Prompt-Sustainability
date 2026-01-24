import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry"]), 7)

    def test_edge_case_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Max_Length(["hello"]), 5)

    def test_edge_case_multiple_element_list(self):
        self.assertEqual(Find_Max_Length(["hello", "world", "python"]), 7)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(Find_Max_Length(["hello", "world", "python", "hello"]), 7)

    def test_edge_case_list_with_empty_string(self):
        self.assertEqual(Find_Max_Length(["hello", "", "world"]), 5)

    def test_edge_case_list_with_empty_string_and_duplicates(self):
        self.assertEqual(Find_Max_Length(["hello", "", "world", "hello"]), 5)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            Find_Max_Length("hello")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            Find_Max_Length(123)
