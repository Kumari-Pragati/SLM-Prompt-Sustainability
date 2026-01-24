import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_true_undulating(self):
        self.assertTrue(is_undulating("abaaba"))

    def test_false_non_undulating(self):
        self.assertFalse(is_undulating("abc"))

    def test_false_too_short(self):
        self.assertFalse(is_undulating("a"))

    def test_true_undulating_with_spaces(self):
        self.assertTrue(is_undulating("a b a b a"))

    def test_false_non_undulating_with_spaces(self):
        self.assertFalse(is_undulating("a b c"))

    def test_true_undulating_with_punctuation(self):
        self.assertTrue(is_undulating("a..a..a"))

    def test_false_non_undulating_with_punctuation(self):
        self.assertFalse(is_undulating("a..b."))
