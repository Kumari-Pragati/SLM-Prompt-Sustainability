import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_typical_case(self):
        text = "I am happily running."
        self.assertEqual(find_adverbs(text), '12-15: happily')

    def test_no_adverb(self):
        text = "I am running."
        self.assertIsNone(find_adverbs(text))

    def test_multiple_adverbs(self):
        text = "I am happily and quickly running."
        self.assertEqual(find_adverbs(text), '12-15: happily')

    def test_adverb_at_start(self):
        text = "happily I am running."
        self.assertEqual(find_adverbs(text), '0-3: happily')

    def test_adverb_at_end(self):
        text = "I am running happily."
        self.assertEqual(find_adverbs(text), '12-15: happily')

    def test_empty_string(self):
        text = ""
        self.assertIsNone(find_adverbs(text))

    def test_whitespace_only(self):
        text = " "
        self.assertIsNone(find_adverbs(text))

    def test_none_input(self):
        with self.assertRaises(TypeError):
            find_adverbs(None)
