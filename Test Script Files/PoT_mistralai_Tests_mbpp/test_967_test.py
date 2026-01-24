import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check("AaEiouUeAiou"), "accepted")

    def test_edge_case_min_length(self):
        self.assertEqual(check("A"), "not accepted")

    def test_edge_case_max_length(self.assertEqual(check("AaEiouUeAiouA"), "accepted"))

    def test_edge_case_exact_5_vowels(self):
        self.assertEqual(check("AaEiou"), "accepted")

    def test_edge_case_exact_6_vowels(self):
        self.assertEqual(check("AaEiouU"), "not accepted")

    def test_edge_case_no_vowels(self):
        self.assertEqual(check("BcDfGhJkLmNpQrStUvWxYz"), "not accepted")

    def test_edge_case_only_one_vowel(self):
        self.assertEqual(check("A"), "not accepted")

    def test_edge_case_only_vowels(self):
        self.assertEqual(check("AaEiou"), "accepted")

    def test_corner_case_duplicate_vowels(self):
        self.assertEqual(check("AaAaEiou"), "accepted")

    def test_corner_case_mixed_case(self):
        self.assertEqual(check("AaEiOuUeAiou"), "accepted")
