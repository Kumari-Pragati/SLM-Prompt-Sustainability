import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_Max_Len_Even("Hello World"), "World")

    def test_edge_case_space_at_start(self):
        self.assertEqual(find_Max_Len_Even("   Hello World"), "Hello")

    def test_edge_case_space_at_end(self):
        self.assertEqual(find_Max_Len_Even("Hello World   "), "World")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(find_Max_Len_Even("Hello   World   "), "World")

    def test_edge_case_no_spaces(self):
        self.assertEqual(find_Max_Len_Even("HelloWorld"), "HelloWorld")

    def test_edge_case_single_space(self):
        self.assertEqual(find_Max_Len_Even("Hello World"), "World")

    def test_edge_case_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_edge_case_single_char(self):
        self.assertEqual(find_Max_Len_Even("a"), "a")

    def test_edge_case_single_word(self):
        self.assertEqual(find_Max_Len_Even("Hello"), "Hello")

    def test_edge_case_multiple_words(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "Hello")

    def test_edge_case_max_len_at_end(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_middle(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_middle(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "Hello")

    def test_edge_case_max_len_at_start_and_end_and_middle(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "Hello")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "Hello")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "Hello")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "Hello")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle(self):
        self.assertEqual(find_Max_Len_Even("Hello World Hello"), "World")

    def test_edge_case_max_len_at_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and_start_and_end_and_middle_and