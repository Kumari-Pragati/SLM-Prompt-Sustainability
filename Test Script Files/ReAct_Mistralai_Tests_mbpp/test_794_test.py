import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_starta_endb('a'), 'Not matched!')

    def test_single_b(self):
        self.assertEqual(text_starta_endb('b'), 'Not matched!')

    def test_multiple_a_and_b(self):
        self.assertEqual(text_starta_endb('aaab'), 'Not matched!')

    def test_match_found_case1(self):
        self.assertEqual(text_starta_endb('aaabcdab'), 'Found a match!')

    def test_match_found_case2(self):
        self.assertEqual(text_starta_endb('aab'), 'Found a match!')

    def test_match_found_case3(self):
        self.assertEqual(text_starta_endb('aabb'), 'Found a match!')

    def test_match_found_case4(self):
        self.assertEqual(text_starta_endb('ab'), 'Found a match!')

    def test_match_found_case5(self):
        self.assertEqual(text_starta_endb('a'), 'Found a match!')

    def test_match_found_case6(self):
        self.assertEqual(text_starta_endb('abab'), 'Found a match!')

    def test_match_found_case7(self):
        self.assertEqual(text_starta_endb('aabab'), 'Found a match!')

    def test_match_found_case8(self):
        self.assertEqual(text_starta_endb('aaabbb'), 'Found a match!')

    def test_match_found_case9(self):
        self.assertEqual(text_starta_endb('aaabbbaa'), 'Found a match!')
