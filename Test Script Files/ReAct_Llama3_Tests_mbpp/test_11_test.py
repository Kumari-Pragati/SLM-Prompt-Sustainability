import unittest
from mbpp_11_code import remove_Occ

class TestRemoveOcc(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Occ("hello world", 'o'), "hell wrld")

    def test_edge_case_start(self):
        self.assertEqual(remove_Occ("hello world", 'h'), "ello wrld")

    def test_edge_case_end(self):
        self.assertEqual(remove_Occ("hello world", 'w'), "hell o rld")

    def test_edge_case_middle(self):
        self.assertEqual(remove_Occ("hello world", 'l'), "heo wrd")

    def test_no_occurrence(self):
        self.assertEqual(remove_Occ("hello world", 'z'), "hello world")

    def test_multiple_occurrences(self):
        self.assertEqual(remove_Occ("hello world hello", 'o'), "hell wrld hell")

    def test_empty_string(self):
        self.assertEqual(remove_Occ("", 'a'), "")

    def test_single_character_string(self):
        self.assertEqual(remove_Occ("a", 'a'), "")

    def test_functionality_with_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_Occ(123, 'a')
