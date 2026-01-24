import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_occurance(""), 0)

    def test_single_char_string(self):
        self.assertEqual(count_occurance("s"), 0)
        self.assertEqual(count_occurance("t"), 0)
        self.assertEqual(count_occurance("d"), 0)

    def test_single_word_string(self):
        self.assertEqual(count_occurance("std"), 0)
        self.assertEqual(count_occurance("std"), 1)
        self.assertEqual(count_occurance("sst"), 0)
        self.assertEqual(count_occurance("tst"), 0)
        self.assertEqual(count_occurance("dstd"), 0)

    def test_multiple_words_string(self):
        self.assertEqual(count_occurance("sstd"), 1)
        self.assertEqual(count_occurance("stdt"), 0)
        self.assertEqual(count_occurance("ststd"), 2)
        self.assertEqual(count_occurance("tstdt"), 0)
        self.assertEqual(count_occurance("dstdst"), 1)

    def test_multiple_occurances(self):
        self.assertEqual(count_occurance("sststd"), 2)
        self.assertEqual(count_occurance("stdstdt"), 1)
        self.assertEqual(count_occurance("ststdst"), 3)
        self.assertEqual(count_occurance("stdstdstd"), 2)
        self.assertEqual(count_occurance("dstdstdst"), 1)
