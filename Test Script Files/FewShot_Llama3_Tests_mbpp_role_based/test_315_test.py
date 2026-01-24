import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Max_Len_Even("Hello World"), "Hello")

    def test_edge_case_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_edge_case_single_word(self):
        self.assertEqual(find_Max_Len_Even("Hello"), "Hello")

    def test_edge_case_single_space(self):
        self.assertEqual(find_Max_Len_Even("   "), "-1")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(find_Max_Len_Even("   Hello   World   "), "Hello")

    def test_edge_case_multiple_spaces_at_start(self):
        self.assertEqual(find_Max_Len_Even("   Hello   World   "), "Hello")

    def test_edge_case_multiple_spaces_at_end(self):
        self.assertEqual(find_Max_Len_Even("Hello   World   "), "Hello")

    def test_edge_case_multiple_spaces_at_start_and_end(self):
        self.assertEqual(find_Max_Len_Even("   Hello   World   "), "Hello")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            find_Max_Len_Even(123)
