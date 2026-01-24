import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_adverbs("quickly"), "0-7: quickly")
        self.assertEqual(find_adverbs("quick"), "0-5: quick")
        self.assertEqual(find_adverbs("quickly quick"), "0-7: quickly 0-5: quick")

    def test_empty(self):
        self.assertIsNone(find_adverbs(""))

    def test_no_adverbs(self):
        self.assertIsNone(find_adverbs("hello world"))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs("quickly quickly"), "0-7: quickly 8-15: quickly")
        self.assertEqual(find_adverbs("quickly quickly quickly"), "0-7: quickly 8-15: quickly 16-23: quickly")

    def test_adverbs_at_end(self):
        self.assertEqual(find_adverbs("quickly hello"), "0-7: quickly")
        self.assertEqual(find_adverbs("quickly quickly hello"), "0-7: quickly 8-15: quickly")
