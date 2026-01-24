import unittest
from mbpp_377_code import remove_Char

class TestRemove_Char(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_Char("hello world", "o"), "hell wrld")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_Char("", "a"), "")

    def test_edge_case_empty_character(self):
        self.assertEqual(remove_Char("hello world", ""), "hello world")

    def test_edge_case_character_not_found(self):
        self.assertEqual(remove_Char("hello world", "x"), "hello world")

    def test_edge_case_multiple_occurrences(self):
        self.assertEqual(remove_Char("hellooo world", "o"), "hell wrld")

    def test_edge_case_character_at_start(self):
        self.assertEqual(remove_Char("ocean", "o"), "cean")

    def test_edge_case_character_at_end(self):
        self.assertEqual(remove_Char("hello world", "d"), "hell world")

    def test_edge_case_character_in_middle(self):
        self.assertEqual(remove_Char("hello world", "l"), "heo wrd")
