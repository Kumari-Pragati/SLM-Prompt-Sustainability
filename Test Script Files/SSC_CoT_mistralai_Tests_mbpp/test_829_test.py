import unittest
from mbpp_829_code import Counter
from 829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(second_frequent("banana"), "a")
        self.assertEqual(second_frequent("apple"), "e")
        self.assertEqual(second_frequent("orange"), "n")

    def test_edge_cases(self):
        self.assertEqual(second_frequent(""), None)
        self.assertEqual(second_frequent("a"), None)
        self.assertEqual(second_frequent("aa"), None)
        self.assertEqual(second_frequent("aaaa"), "a")

    def test_boundary_cases(self):
        self.assertEqual(second_frequent("bananana"), "n")
        self.assertEqual(second_frequent("bananaa"), "a")
        self.assertEqual(second_frequent("banananana"), "n")

    def test_special_cases(self):
        self.assertEqual(second_frequent("abab"), "b")
        self.assertEqual(second_frequent("ababa"), None)
