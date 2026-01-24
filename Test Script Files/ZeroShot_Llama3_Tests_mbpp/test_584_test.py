import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_find_adverbs(self):
        self.assertEqual(find_adverbs("I am happy"), "0-7: happy")
        self.assertEqual(find_adverbs("I am very happy"), "5-11: very")
        self.assertEqual(find_adverbs("I am extremely happy"), "9-17: extremely")
        self.assertEqual(find_adverbs("I am not happy"), "0-7: not")
        self.assertEqual(find_adverbs("I am not very happy"), "5-11: very")
        self.assertEqual(find_adverbs("I am not extremely happy"), "9-17: extremely")
        self.assertEqual(find_adverbs("I am not extremely happy today"), "9-17: extremely")
        self.assertEqual(find_adverbs("I am not extremely happy today but I am happy"), "0-7: happy")
        self.assertEqual(find_adverbs("I am not extremely happy today but I am very happy"), "5-11: very")
        self.assertEqual(find_adverbs("I am not extremely happy today but I am extremely happy"), "9-17: extremely")
        self.assertEqual(find_adverbs("I am not extremely happy today but I am extremely happy now"), "9-17: extremely")

    def test_find_adverbs_empty_string(self):
        self.assertEqual(find_adverbs(""), "")

    def test_find_adverbs_no_adverbs(self):
        self.assertEqual(find_adverbs("I am a person"), "")
