import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_adverbs("quickly run slowly"), "0-4: quickly 13-17: slowly")
        self.assertEqual(find_adverbs("I am very carefully walking"), "10-14: carefully 21-25: walking")

    def test_edge_case_single_word(self):
        self.assertEqual(find_adverbs("happily"), "0-5: happily")
        self.assertEqual(find_adverbs("angrily"), "0-6: angrily")

    def test_edge_case_no_match(self):
        self.assertEqual(find_adverbs("hello world"), "")
        self.assertEqual(find_adverbs("quick"), "")

    def test_edge_case_multiple_adverbs(self):
        self.assertEqual(find_adverbs("quickly run slowly and loudly"), "0-4: quickly 13-17: slowly 26-30: loudly")

    def test_edge_case_adverb_at_start_and_end(self):
        self.assertEqual(find_adverbs("only slowly at the end quickly at the beginning"), "0-4: quickly 24-28: slowly 41-45: quickly")

    def test_edge_case_adverb_in_middle_of_word(self):
        self.assertEqual(find_adverbs("unhappily"), "0-7: unhappily")
        self.assertEqual(find_adverbs("unangrily"), "0-8: unangrily")
