import unittest
from mbpp_254_code import words_ae

class TestWordsAe(unittest.TestCase):

    def test_words_ae(self):
        self.assertEqual(words_ae("The aardvark ate an apple"), ["aardvark", "ate", "an"])
        self.assertEqual(words_ae("The aardvark ate an aeolian"), ["aardvark", "ate", "aeolian"])
        self.assertEqual(words_ae("The aardvark ate an aeolian apple"), ["aardvark", "ate", "aeolian", "apple"])
        self.assertEqual(words_ae(""), [])
        self.assertEqual(words_ae("The aardvark ate an apple ae"), ["aardvark", "ate", "an", "ae"])
        self.assertEqual(words_ae("The aardvark ate an aeolian ae"), ["aardvark", "ate", "aeolian", "ae"])

