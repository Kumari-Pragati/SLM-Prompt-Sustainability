import unittest
from mbpp_305_code import start_withp

class TestStartWithP(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(start_withp([]))

    def test_single_word(self):
        self.assertIsNone(start_withp(["apple"]))
        self.assertIsNone(start_withp(["Papaya"]))

    def test_multiple_words(self):
        self.assertIsNone(start_withp(["ApplePear", "OrangeBanana"]))
        self.assertIsNone(start_withp(["PineapplePeach", "GrapeMango"]))

    def test_words_with_matches(self):
        self.assertEqual(start_withp(["PApEr", "PhOnE"]), ("PApEr", "PhOnE"))
        self.assertEqual(start_withp(["pApEr", "pHOnE"]), ("pApEr", "pHOnE"))
        self.assertEqual(start_withp(["PaPa", "PhOe"]), (None, None))
