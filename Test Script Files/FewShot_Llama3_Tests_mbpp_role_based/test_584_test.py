import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_typical_use_case(self):
        text = "The sun sets slowly in the west."
        self.assertEqual(find_adverbs(text), "0-9: slowly")

    def test_multiple_adverbs(self):
        text = "The sun sets slowly in the west, and the moon rises quickly."
        self.assertEqual(find_adverbs(text), "0-7: slowly 14-19: quickly")

    def test_no_adverbs(self):
        text = "The sun sets in the west."
        self.assertEqual(find_adverbs(text), "")

    def test_edge_case_empty_string(self):
        text = ""
        self.assertEqual(find_adverbs(text), "")

    def test_edge_case_single_word(self):
        text = "Hello"
        self.assertEqual(find_adverbs(text), "")

    def test_edge_case_single_adverb(self):
        text = "The sun sets slowly."
        self.assertEqual(find_adverbs(text), "0-9: slowly")
