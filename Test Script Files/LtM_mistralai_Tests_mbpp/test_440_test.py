import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_adverb_position("quickly"), (3, 7, "quickly"))
        self.assertEqual(find_adverb_position("slowly"), (5, 10, "slowly"))

    def test_edge_and_boundary(self):
        self.assertEqual(find_adverb_position(""), (0, 0, None))
        self.assertEqual(find_adverb_position("quickly, slowly"), (7, 13, "quickly"))
        self.assertEqual(find_adverb_position("quickly, slowly, quickly"), (14, 20, "quickly"))
        self.assertEqual(find_adverb_position("quicklyly"), (0, 5, "quicklyly"))
        self.assertEqual(find_adverb_position("adverbly"), (4, 9, "adverbly"))

    def test_complex(self):
        self.assertEqual(find_adverb_position("The cat quickly ran slowly across the street."),
                         (24, 33, "quickly"))
        self.assertEqual(find_adverb_position("The cat, now slowly, ran quickly across the street."),
                         (34, 43, "quickly"))
        self.assertEqual(find_adverb_position("The cat, now slowly, ran, and then quickly, across the street."),
                         (44, 53, "quickly"))
