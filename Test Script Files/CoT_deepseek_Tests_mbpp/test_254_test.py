import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):

    def test_typical_case(self):
        text = "apple aeroplane aerobic"
        expected_output = ['apple', 'aeroplane', 'aerobic']
        self.assertEqual(words_ae(text), expected_output)

    def test_single_word_with_ae(self):
        text = "aer"
        expected_output = ['aer']
        self.assertEqual(words_ae(text), expected_output)

    def test_single_word_without_ae(self):
        text = "apple"
        expected_output = []
        self.assertEqual(words_ae(text), expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = []
        self.assertEqual(words_ae(text), expected_output)

    def test_string_with_no_ae(self):
        text = "banana orange"
        expected_output = []
        self.assertEqual(words_ae(text), expected_output)

    def test_string_with_ae_at_end(self):
        text = "apple aeroplane aerobic"
        expected_output = ['apple', 'aeroplane', 'aerobic']
        self.assertEqual(words_ae(text), expected_output)

    def test_string_with_ae_at_start(self):
        text = "aer aeroplane aerobic"
        expected_output = ['aer', 'aeroplane', 'aerobic']
        self.assertEqual(words_ae(text), expected_output)

    def test_string_with_ae_at_both_ends(self):
        text = "aer aeroplane aerobic aer"
        expected_output = ['aer', 'aeroplane', 'aerobic', 'aer']
        self.assertEqual(words_ae(text), expected_output)
