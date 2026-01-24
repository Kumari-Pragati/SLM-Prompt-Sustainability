import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(long_words(5, "apple banana cherry orange"), ["cherry", "orange"])
        self.assertListEqual(long_words(3, "ant elephant"), ["elephant"])
        self.assertListEqual(long_words(4, "cat dog fish"), [])

    def test_edge_case(self):
        self.assertListEqual(long_words(0, "apple"), [])
        self.assertListEqual(long_words(1, "ant"), ["ant"])
        self.assertListEqual(long_words(len("ant"), "ant"), ["ant"])

    def test_boundary_case(self):
        self.assertListEqual(long_words(len("ant") + 1, "ant"), [])
        self.assertListEqual(long_words(len("ant") - 1, "ant elephant"), ["elephant"])
