import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_simple_adverb(self):
        self.assertEqual(find_adverbs("quickly"), "0-5: quickly")

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs("slowly and quickly"), "5-10: quickly")

    def test_adverb_at_beginning(self):
        self.assertEqual(find_adverbs("ly quick"), "0-1: ly")

    def test_adverb_at_end(self):
        self.assertEqual(find_adverbs("quick ly"), "10-11: ly")

    def test_adverb_in_middle(self):
        self.assertEqual(find_adverbs("quickly and slowly"), "5-10: quickly")

    def test_empty_string(self):
        self.assertEqual(find_adverbs(""), "")

    def test_no_adverbs(self):
        self.assertEqual(find_adverbs("quick"), "")

    def test_adverb_with_number(self):
        self.assertEqual(find_adverbs("twentyly"), "")

    def test_adverb_with_special_characters(self):
        self.assertEqual(find_adverbs("quickly,ly"), "")
