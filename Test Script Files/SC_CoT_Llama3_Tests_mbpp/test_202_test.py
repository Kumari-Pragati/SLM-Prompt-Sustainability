import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_even("abcdef"), "bd")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_even(""), "")

    def test_edge_case_single_character(self):
        self.assertEqual(remove_even("a"), "a")

    def test_edge_case_single_even_character(self):
        self.assertEqual(remove_even("even"), "")

    def test_edge_case_single_odd_character(self):
        self.assertEqual(remove_even("odd"), "o")

    def test_edge_case_single_even_character_at_end(self):
        self.assertEqual(remove_even("evenodd"), "od")

    def test_edge_case_single_odd_character_at_end(self):
        self.assertEqual(remove_even("evenodd"), "eveno")

    def test_edge_case_all_even_characters(self):
        self.assertEqual(remove_even("eveneven"), "")

    def test_edge_case_all_odd_characters(self):
        self.assertEqual(remove_even("oddodd"), "odod")

    def test_edge_case_mixed_characters(self):
        self.assertEqual(remove_even("evenodd"), "od")

    def test_edge_case_mixed_characters_at_start(self):
        self.assertEqual(remove_even("evenodd"), "od")

    def test_edge_case_mixed_characters_at_end(self):
        self.assertEqual(remove_even("evenodd"), "od")

    def test_edge_case_mixed_characters_at_start_and_end(self):
        self.assertEqual(remove_even("evenodd"), "od")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_even(123)

    def test_invalid_input_non_string_type(self):
        with self.assertRaises(TypeError):
            remove_even(None)
