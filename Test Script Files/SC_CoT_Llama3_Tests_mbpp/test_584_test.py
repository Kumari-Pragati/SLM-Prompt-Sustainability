import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_adverbs("Hello, world!"), "0-7: Hello")

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs("This is a test, very well!"), "4-8: is")
        self.assertEqual(find_adverbs("This is a test, very well!"), "13-19: well")

    def test_edge_case_empty_string(self):
        self.assertIsNone(find_adverbs(""))

    def test_edge_case_single_word(self):
        self.assertEqual(find_adverbs("Hello"), None)

    def test_edge_case_no_adverbs(self):
        self.assertIsNone(find_adverbs("This is a test"))

    def test_edge_case_single_adverb(self):
        self.assertEqual(find_adverbs("Hello, quickly!"), "11-18: quickly")

    def test_edge_case_multiple_adverbs(self):
        self.assertEqual(find_adverbs("This is a test, very well, quickly!"), "4-8: is")
        self.assertEqual(find_adverbs("This is a test, very well, quickly!"), "13-19: well")
        self.assertEqual(find_adverbs("This is a test, very well, quickly!"), "24-30: quickly")

    def test_edge_case_multiple_adverbs_with_spaces(self):
        self.assertEqual(find_adverbs("This is a test, very well, quickly, quickly!"), "4-8: is")
        self.assertEqual(find_adverbs("This is a test, very well, quickly, quickly!"), "13-19: well")
        self.assertEqual(find_adverbs("This is a test, very well, quickly, quickly!"), "24-30: quickly")
        self.assertEqual(find_adverbs("This is a test, very well, quickly, quickly!"), "35-41: quickly")
