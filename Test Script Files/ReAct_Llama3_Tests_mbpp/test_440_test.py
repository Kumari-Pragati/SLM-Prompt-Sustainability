import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_adverb_position("Hello worldly goodbye"), ((6, 13, 'worldly')))

    def test_edge_case_no_match(self):
        self.assertIsNone(find_adverb_position("Hello world goodbye"))

    def test_edge_case_multiple_matches(self):
        self.assertEqual(find_adverb_position("Hello worldly goodbye worldly"), ((6, 13, 'worldly'), (14, 21, 'worldly')))

    def test_edge_case_empty_string(self):
        self.assertIsNone(find_adverb_position(""))

    def test_edge_case_single_character(self):
        self.assertIsNone(find_adverb_position("a"))

    def test_edge_case_single_word(self):
        self.assertIsNone(find_adverb_position("world"))

    def test_edge_case_single_character_space(self):
        self.assertIsNone(find_adverb_position(" "))

    def test_edge_case_single_word_space(self):
        self.assertIsNone(find_adverb_position(" world"))

    def test_edge_case_multiple_spaces(self):
        self.assertIsNone(find_adverb_position("  "))

    def test_edge_case_multiple_spaces_and_word(self):
        self.assertIsNone(find_adverb_position("  world "))

    def test_edge_case_multiple_spaces_and_wordly(self):
        self.assertEqual(find_adverb_position("  worldly  "), ((6, 13, 'worldly')))
