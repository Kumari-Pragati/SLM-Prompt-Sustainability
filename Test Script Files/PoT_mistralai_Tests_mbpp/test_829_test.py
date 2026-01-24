import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(second_frequent("banana"), "a")
        self.assertEqual(second_frequent("apple"), None)
        self.assertEqual(second_frequent("zebra"), None)

    def test_edge_case_single_element(self):
        self.assertEqual(second_frequent("a"), "a")
        self.assertEqual(second_frequent(""), None)

    def test_edge_case_two_elements(self):
        self.assertEqual(second_frequent("aa"), None)
        self.assertEqual(second_frequent("ab"), "b")

    def test_edge_case_tie(self):
        self.assertEqual(second_frequent("aaa"), "a")
        self.assertEqual(second_frequent("abab"), None)
