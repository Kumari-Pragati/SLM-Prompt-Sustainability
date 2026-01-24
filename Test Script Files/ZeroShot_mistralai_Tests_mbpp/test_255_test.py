import unittest
from mbpp_255_code import combinations_with_replacement

def combinations_colors(l, n):
    return list(combinations_with_replacement(l,n))

class TestCombinationsColors(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(combinations_colors([], 3), [])

    def test_single_element(self):
        self.assertListEqual(combinations_colors(["A"], 3), [["A", "A", "A"]])

    def test_two_elements(self):
        self.assertListEqual(combinations_colors(["A", "B"], 2), [["A", "A"], ["A", "B"], ["B", "A"], ["B", "B"]])

    def test_three_elements(self):
        self.assertListEqual(combinations_colors(["A", "B", "C"], 3), [["A", "B", "C"], ["A", "B", "A"], ["A", "C", "B"], ["B", "A", "C"], ["B", "C", "A"], ["C", "A", "B"], ["A", "A", "B"], ["A", "A", "C"], ["A", "B", "A"], ["B", "A", "A"], ["B", "B", "C"], ["B", "C", "A"], ["C", "A", "B"], ["C", "B", "A"]])

    def test_four_elements(self):
        self.assertListEqual(combinations_colors(["A", "B", "C", "D"], 4), [["A", "B", "C", "D"], ["A", "B", "C", "A"], ["A", "B", "D", "C"], ["A", "C", "B", "D"], ["A", "C", "D", "B"], ["A", "D", "B", "C"], ["B", "A", "C", "D"], ["B", "A", "D", "C"], ["B", "C", "A", "D"], ["B", "C", "D", "A"], ["B", "D", "A", "C"], ["B", "D", "C", "A"], ["C", "A", "B", "D"], ["C", "A", "D", "B"], ["C", "B", "A", "D"], ["C", "B", "D", "A"], ["C", "D", "A", "B"], ["C", "D", "B", "A"], ["D", "A", "B", "C"], ["D", "A", "C", "B"], ["D", "B", "A", "C"], ["D", "B", "C", "A"]])
