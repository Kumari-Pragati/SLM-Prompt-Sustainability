import unittest
from mbpp_254_code import words_ae

class TestWordsAe(unittest.TestCase):
    def test_typical_use_case(self):
        text = "The aeolian harp plays a gentle aeolian melody."
        self.assertEqual(words_ae(text), ["aeolian", "aeolian"])

    def test_multiple_occurrences(self):
        text = "The aeolian harp plays a gentle aeolian melody. Aeolian music is beautiful."
        self.assertEqual(words_ae(text), ["aeolian", "aeolian", "Aeolian"])

    def test_case_insensitivity(self):
        text = "The AEOLIAN harp plays a gentle aeolian melody."
        self.assertEqual(words_ae(text), ["AEOLIAN", "aeolian"])

    def test_no_matches(self):
        text = "The sun is shining brightly today."
        self.assertEqual(words_ae(text), [])

    def test_empty_string(self):
        text = ""
        self.assertEqual(words_ae(text), [])
