import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(long_words(4, "apple banana cherry"), ["cherry"])
        self.assertListEqual(long_words(5, "apple banana cherry"), ["apple", "cherry"])
        self.assertListEqual(long_words(3, "one two three"), ["three"])

    def test_edge_cases(self):
        self.assertListEqual(long_words(1, "apple banana cherry"), [])
        self.assertListEqual(long_words(len("apple"), "apple"), ["apple"])
        self.assertListEqual(long_words(0, "apple banana cherry"), [])

    def test_complex(self):
        self.assertListEqual(long_words(4, "apple banana apple apple apple"), ["apple", "apple", "apple"])
        self.assertListEqual(long_words(3, "apple apple apple banana"), ["banana"])
        self.assertListEqual(long_words(2, "apple apple apple apple apple apple apple"), ["apple", "apple"])
