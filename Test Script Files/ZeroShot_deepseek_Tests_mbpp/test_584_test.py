import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_adverb_found(self):
        self.assertEqual(find_adverbs('I am happily walking'), '6-12: happily')

    def test_adverb_not_found(self):
        self.assertIsNone(find_adverbs('I am walking'))

    def test_empty_string(self):
        self.assertIsNone(find_adverbs(''))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs('I am happily and quickly walking'), '6-12: happily')
