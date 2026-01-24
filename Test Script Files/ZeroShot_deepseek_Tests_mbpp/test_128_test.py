import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_long_words(self):
        self.assertEqual(long_words(3, "the quick brown fox"), ["brown", "quick"])
        self.assertEqual(long_words(5, "the long and winding road"), ["long", "winding", "road"])
        self.assertEqual(long_words(0, "the quick brown fox"), [])
        self.assertEqual(long_words(10, ""), [])
        self.assertEqual(long_words(2, "a b c d e f g h i j k l m n o p q r s t u v w x y z"), [])
