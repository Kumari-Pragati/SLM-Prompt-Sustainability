import unittest
from mbpp_338_code import count_Substring_WithEqualEnds

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_SubstringWithEqualEnds(''), 0)

    def test_single_character(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(count_SubstringWithEqualEnds(char), 1)

    def test_palindrome(self):
        self.assertEqual(count_SubstringWithEqualEnds('racecar'), 5)
        self.assertEqual(count_SubstringWithEqualEnds('level'), 2)

    def test_non_palindrome(self):
        self.assertEqual(count_SubstringWithEqualEnds('hello'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('python'), 0)

    def test_mixed_case(self):
        self.assertEqual(count_SubstringWithEqualEnds('HeLLo'), 1)
        self.assertEqual(count_SubstringWithEqualEnds('PyThOn'), 1)

    def test_long_string(self):
        self.assertEqual(count_SubstringWithEqualEnds('aardvark'), 1)
        self.assertEqual(count_SubstringWithEqualEnds('zebras'), 0)

    def test_edge_cases(self):
        self.assertEqual(count_SubstringWithEqualEnds(''), 0)
        self.assertEqual(count_SubstringWithEqualEnds('a'), 1)
        self.assertEqual(count_SubstringWithEqualEnds('aa'), 1)
        self.assertEqual(count_SubstringWithEqualEnds('ab'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('aab'), 1)
        self.assertEqual(count_SubstringWithEqualEnds('abc'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcd'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcde'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdef'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefg'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefgh'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghi'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghij'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghijk'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghijl'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghijm'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghijn'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghijno'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghijpq'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghijrst'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghijuvw'), 0)
        self.assertEqual(count_SubstringWithEqualEnds('abcdefghijxyz'), 0)
