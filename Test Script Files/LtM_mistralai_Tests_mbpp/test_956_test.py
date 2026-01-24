import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):
    def test_simple(self):
        self.assertListEqual(split_list("A"), ["A"])
        self.assertListEqual(split_list("AB"), ["AB"])
        self.assertListEqual(split_list("ABC"), ["AB", "C"])

    def test_edge_cases(self):
        self.assertListEqual(split_list("A "), ["A"])
        self.assertListEqual(split_list(" A "), ["A"])
        self.assertListEqual(split_list("Aa"), [])
        self.assertListEqual(split_list("A1"), [])
        self.assertListEqual(split_list("1A"), [])
        self.assertListEqual(split_list("1A1"), [])

    def test_complex(self):
        self.assertListEqual(split_list("ABC123"), ["AB", "C"])
        self.assertListEqual(split_list("123ABC"), [])
        self.assertListEqual(split_list("ABC123ABC"), ["AB", "C", "AB"])
        self.assertListEqual(split_list("ABC123ABC123"), ["AB", "C", "AB"])
        self.assertListEqual(split_list("ABC123ABC123XYZ"), ["AB", "C", "AB"])
        self.assertListEqual(split_list("ABC123ABC123XYZ123"), ["AB", "C", "AB"])
