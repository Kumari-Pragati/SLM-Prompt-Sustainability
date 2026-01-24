import unittest
from mbpp_182_code import find_character

class TestFindCharacter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_character("Hello, World! 123"), 
                         (['H', 'W'], ['e', 'o', 'r', 'l', 'd'], ['1', '2', '3'], ['', ',','', '!']))

    def test_edge_case_empty_string(self):
        self.assertEqual(find_character(""), 
                         ([], [], [], []))

    def test_edge_case_single_character(self):
        self.assertEqual(find_character("A"), 
                         (['A'], [], [], []))

    def test_edge_case_single_digit(self):
        self.assertEqual(find_character("1"), 
                         ([], [], ['1'], []))

    def test_edge_case_single_punctuation(self):
        self.assertEqual(find_character("!"), 
                         ([], [], [], ['!']))

    def test_edge_case_multiple_types(self):
        self.assertEqual(find_character("Hello123, World!"), 
                         (['H', 'W'], ['e', 'o', 'r', 'l', 'd'], ['1', '2', '3'], [', ','', '!']))

    def test_edge_case_no_characters(self):
        self.assertEqual(find_character("   "), 
                         ([], [], [], []))
