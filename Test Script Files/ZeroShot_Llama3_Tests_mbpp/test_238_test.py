import unittest
from mbpp_238_code import number_of_substrings

class TestNumberOfSubstrings(unittest.TestCase):

    def test_number_of_substrings(self):
        self.assertEqual(number_of_substrings(""), 0)
        self.assertEqual(number_of_substrings("a"), 1)
        self.assertEqual(number_of_substrings("ab"), 3)
        self.assertEqual(number_of_substrings("abc"), 6)
        self.assertEqual(number_of_substrings("abcd"), 10)
        self.assertEqual(number_of_substrings("abcde"), 15)
        self.assertEqual(number_of_substrings("abcdef"), 21)
        self.assertEqual(number_of_substrings("abcdefg"), 28)
        self.assertEqual(number_of_substrings("abcdefgh"), 36)
        self.assertEqual(number_of_substrings("abcdefghi"), 45)
        self.assertEqual(number_of_substrings("abcdefghij"), 55)
        self.assertEqual(number_of_substrings("abcdefghijk"), 66)
        self.assertEqual(number_of_substrings("abcdefghijkl"), 78)
        self.assertEqual(number_of_substrings("abcdefghijklm"), 91)
        self.assertEqual(number_of_substrings("abcdefghijklmn"), 105)
        self.assertEqual(number_of_substrings("abcdefghijklmno"), 120)
        self.assertEqual(number_of_substrings("abcdefghijklmnop"), 136)
        self.assertEqual(number_of_substrings("abcdefghijklmnopq"), 153)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqr"), 171)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrs"), 190)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrst"), 210)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstu"), 231)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuv"), 253)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuvw"), 276)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuvwx"), 300)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuvwxy"), 325)
        self.assertEqual(number_of_substrings("abcdefghijklmnopqrstuvwxyz"), 351)
