import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):
    def test_normal_case(self):
        self.assertListEqual(split_list("ABC DEF GHI"), ["ABC", "DEF", "GHI"])

    def test_edge_case_empty(self):
        self.assertListEqual(split_list(""), [])

    def test_edge_case_single_word(self):
        self.assertListEqual(split_list("XYZ"), ["XYZ"])

    def test_edge_case_single_letter(self):
        self.assertListEqual(split_list("A"), ["A"])

    def test_edge_case_only_numbers(self):
        self.assertListEqual(split_list("12345"), [])

    def test_edge_case_only_punctuation(self):
        self.assertListEqual(split_list("!@#$%^&*()"), [])

    def test_edge_case_only_spaces(self):
        self.assertListEqual(split_list("   "), [])

    def test_edge_case_mixed_case(self):
        self.assertListEqual(split_list("aBc DeF gHi"), ["aBc", "DeF", "gHi"])

    def test_edge_case_special_characters(self):
        self.assertListEqual(split_list("AbC_dEf_gHi#$%^&*()"), ["AbC", "dEf", "gHi"])

    def test_invalid_input(self):
        self.assertRaises(TypeError, split_list, 123)
