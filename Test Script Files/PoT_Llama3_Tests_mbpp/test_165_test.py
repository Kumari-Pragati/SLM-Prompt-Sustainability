import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_char_position("Hello"), 2)

    def test_edge_case(self):
        self.assertEqual(count_char_position("abc"), 0)

    def test_edge_case2(self):
        self.assertEqual(count_char_position("ABC"), 0)

    def test_edge_case3(self):
        self.assertEqual(count_char_position("123"), 0)

    def test_edge_case4(self):
        self.assertEqual(count_char_position("aA"), 2)

    def test_edge_case5(self):
        self.assertEqual(count_char_position("abcABC"), 2)

    def test_edge_case6(self):
        self.assertEqual(count_char_position("aAbB"), 4)

    def test_edge_case7(self):
        self.assertEqual(count_char_position("aAaA"), 4)

    def test_edge_case8(self):
        self.assertEqual(count_char_position("aAaAbB"), 6)

    def test_edge_case9(self):
        self.assertEqual(count_char_position("aAaAbBcC"), 6)

    def test_edge_case10(self):
        self.assertEqual(count_char_position("aAaAbBcCdD"), 6)

    def test_edge_case11(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeE"), 6)

    def test_edge_case12(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeEfF"), 6)

    def test_edge_case13(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeEfFgG"), 6)

    def test_edge_case14(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeEfFgGhH"), 6)

    def test_edge_case15(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeEfFgGhHiI"), 6)

    def test_edge_case16(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeEfFgGhHiIjJ"), 6)

    def test_edge_case17(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeEfFgGhHiIjJkK"), 6)

    def test_edge_case18(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeEfFgGhHiIjJkKlL"), 6)

    def test_edge_case19(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeEfFgGhHiIjJkKlLmM"), 6)

    def test_edge_case20(self):
        self.assertEqual(count_char_position("aAaAbBcCdDeEfFgGhHiIjJkKlLmMnN"), 6)
