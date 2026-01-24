import unittest
from mbpp_776_code import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_single_char(self):
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("e"), 1)
        self.assertEqual(count_vowels("i"), 1)
        self.assertEqual(count_vowels("o"), 1)
        self.assertEqual(count_vowels("u"), 1)
        self.assertEqual(count_vowels("b"), 0)
        self.assertEqual(count_vowels("c"), 0)
        self.assertEqual(count_vowels("d"), 0)
        self.assertEqual(count_vowels("f"), 0)
        self.assertEqual(count_vowels("g"), 0)
        self.assertEqual(count_vowels("h"), 0)
        self.assertEqual(count_vowels("j"), 0)
        self.assertEqual(count_vowels("k"), 0)
        self.assertEqual(count_vowels("l"), 0)
        self.assertEqual(count_vowels("m"), 0)
        self.assertEqual(count_vowels("n"), 0)
        self.assertEqual(count_vowels("p"), 0)
        self.assertEqual(count_vowels("q"), 0)
        self.assertEqual(count_vowels("r"), 0)
        self.assertEqual(count_vowels("s"), 0)
        self.assertEqual(count_vowels("t"), 0)
        self.assertEqual(count_vowels("v"), 0)
        self.assertEqual(count_vowels("w"), 0)
        self.assertEqual(count_vowels("x"), 0)
        self.assertEqual(count_vowels("y"), 0)
        self.assertEqual(count_vowels("z"), 0)

    def test_multiple_chars(self):
        self.assertEqual(count_vowels("abc"), 0)
        self.assertEqual(count_vowels("def"), 0)
        self.assertEqual(count_vowels("ghi"), 0)
        self.assertEqual(count_vowels("jkl"), 0)
        self.assertEqual(count_vowels("mno"), 0)
        self.assertEqual(count_vowels("pqr"), 0)
        self.assertEqual(count_vowels("stu"), 0)
        self.assertEqual(count_vowels("vwx"), 0)
        self.assertEqual(count_vowels("yz"), 0)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("aeioua"), 5)
        self.assertEqual(count_vowels("aeioue"), 5)
        self.assertEqual(count_vowels("aeiouo"), 5)
        self.assertEqual(count_vowels("aeiouu"), 5)

    def test_edge_cases(self):
        self.assertEqual(count_vowels("a"), 1)
        self.assertEqual(count_vowels("e"), 1)
        self.assertEqual(count_vowels("i"), 1)
        self.assertEqual(count_vowels("o"), 1)
        self.assertEqual(count_vowels("u"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("aeioua"), 5)
        self.assertEqual(count_vowels("aeioue"), 5)
        self.assertEqual(count_vowels("aeiouo"), 5)
        self.assertEqual(count_vowels("aeiouu"), 5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_vowels(123)
