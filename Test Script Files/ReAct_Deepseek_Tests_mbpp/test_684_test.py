import unittest
from mbpp_684_code import count_Char

class TestCountChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Char("hello", 'l'), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Char("", 'a'), 0)

    def test_edge_case_string_with_one_char(self):
        self.assertEqual(count_Char("a", 'a'), 1)
        self.assertEqual(count_Char("a", 'b'), 0)

    def test_edge_case_string_with_same_char(self):
        self.assertEqual(count_Char("aaaaa", 'a'), 5)

    def test_edge_case_string_with_different_char(self):
        self.assertEqual(count_Char("abc", 'd'), 0)

    def test_edge_case_n_is_zero(self):
        self.assertEqual(count_Char("abc", 'a'), 0)

    def test_edge_case_n_is_less_than_length_of_string(self):
        self.assertEqual(count_Char("abc", 'a'), 1)

    def test_edge_case_n_is_equal_to_length_of_string(self):
        self.assertEqual(count_Char("abc", 'a'), 1)

    def test_edge_case_n_is_greater_than_length_of_string(self):
        self.assertEqual(count_Char("abc", 'a'), 1)
